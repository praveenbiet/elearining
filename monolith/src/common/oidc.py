from typing import Optional

from authlib.integrations.starlette_client import OAuth
from fastapi import HTTPException, Request
from starlette.config import Config

from .config import get_settings
from .logger import get_logger

settings = get_settings()
logger = get_logger(__name__)

# Create OAuth config
oauth_config = Config(
    environ={
        "OIDC_ISSUER": settings.OIDC_ISSUER,
        "OIDC_CLIENT_ID": settings.OIDC_CLIENT_ID,
        "OIDC_CLIENT_SECRET": settings.OIDC_CLIENT_SECRET,
    }
)

# Create OAuth client
oauth = OAuth(oauth_config)
oauth.register(
    name="oidc",
    server_metadata_url=f"{settings.OIDC_ISSUER}/.well-known/openid-configuration",
    client_kwargs={"scope": "openid email profile"},
)


async def get_oidc_user(request: Request) -> Optional[dict]:
    """Get the current user from OIDC session."""
    try:
        user = request.session.get("user")
        if not user:
            return None
        return user
    except Exception as e:
        logger.error(
            "Failed to get OIDC user",
            extra={
                "error": str(e),
            },
        )
        raise


async def require_oidc_auth(request: Request) -> dict:
    """Require OIDC authentication and return the user."""
    user = await get_oidc_user(request)
    if not user:
        raise HTTPException(
            status_code=401,
            detail="Not authenticated",
        )
    return user


async def login_oidc(request: Request) -> str:
    """Initiate OIDC login flow."""
    try:
        redirect_uri = request.url_for("auth_callback")
        return await oauth.oidc.authorize_redirect(request, redirect_uri)
    except Exception as e:
        logger.error(
            "Failed to initiate OIDC login",
            extra={
                "error": str(e),
            },
        )
        raise


async def callback_oidc(request: Request) -> dict:
    """Handle OIDC callback."""
    try:
        token = await oauth.oidc.authorize_access_token(request)
        user = await oauth.oidc.parse_id_token(request, token)
        request.session["user"] = user
        return user
    except Exception as e:
        logger.error(
            "Failed to handle OIDC callback",
            extra={
                "error": str(e),
            },
        )
        raise


async def logout_oidc(request: Request) -> None:
    """Logout from OIDC."""
    try:
        request.session.pop("user", None)
    except Exception as e:
        logger.error(
            "Failed to logout from OIDC",
            extra={
                "error": str(e),
            },
        )
        raise


async def get_access_token(request: Request) -> Optional[str]:
    """Get the OIDC access token."""
    try:
        token = request.session.get("token")
        if not token:
            return None
        return token["access_token"]
    except Exception as e:
        logger.error(
            "Failed to get access token",
            extra={
                "error": str(e),
            },
        )
        raise


async def refresh_access_token(request: Request) -> Optional[str]:
    """Refresh the OIDC access token."""
    try:
        token = request.session.get("token")
        if not token or "refresh_token" not in token:
            return None
        new_token = await oauth.oidc.refresh_token(
            request,
            token["refresh_token"],
        )
        request.session["token"] = new_token
        return new_token["access_token"]
    except Exception as e:
        logger.error(
            "Failed to refresh access token",
            extra={
                "error": str(e),
            },
        )
        raise 