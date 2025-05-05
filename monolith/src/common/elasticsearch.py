from typing import Any, Dict, List, Optional

from elasticsearch import AsyncElasticsearch
from elasticsearch.exceptions import NotFoundError

from .config import get_settings
from .logger import get_logger

settings = get_settings()
logger = get_logger(__name__)

# Create Elasticsearch client
es_client = AsyncElasticsearch(
    hosts=[f"{settings.ELASTICSEARCH_HOST}:{settings.ELASTICSEARCH_PORT}"],
    http_auth=(
        settings.ELASTICSEARCH_USERNAME,
        settings.ELASTICSEARCH_PASSWORD,
    ) if settings.ELASTICSEARCH_USERNAME and settings.ELASTICSEARCH_PASSWORD else None,
)


async def create_index(index: str, mappings: Dict[str, Any]) -> bool:
    """Create an Elasticsearch index with mappings."""
    try:
        if not await es_client.indices.exists(index=index):
            await es_client.indices.create(
                index=index,
                body={"mappings": mappings},
            )
            logger.info(
                "Index created",
                extra={
                    "index": index,
                },
            )
            return True
        return False
    except Exception as e:
        logger.error(
            "Failed to create index",
            extra={
                "index": index,
                "error": str(e),
            },
        )
        raise


async def delete_index(index: str) -> bool:
    """Delete an Elasticsearch index."""
    try:
        if await es_client.indices.exists(index=index):
            await es_client.indices.delete(index=index)
            logger.info(
                "Index deleted",
                extra={
                    "index": index,
                },
            )
            return True
        return False
    except Exception as e:
        logger.error(
            "Failed to delete index",
            extra={
                "index": index,
                "error": str(e),
            },
        )
        raise


async def index_document(index: str, id: str, document: Dict[str, Any]) -> bool:
    """Index a document in Elasticsearch."""
    try:
        await es_client.index(
            index=index,
            id=id,
            body=document,
        )
        logger.debug(
            "Document indexed",
            extra={
                "index": index,
                "id": id,
            },
        )
        return True
    except Exception as e:
        logger.error(
            "Failed to index document",
            extra={
                "index": index,
                "id": id,
                "error": str(e),
            },
        )
        raise


async def get_document(index: str, id: str) -> Optional[Dict[str, Any]]:
    """Get a document from Elasticsearch."""
    try:
        response = await es_client.get(
            index=index,
            id=id,
        )
        return response["_source"]
    except NotFoundError:
        return None
    except Exception as e:
        logger.error(
            "Failed to get document",
            extra={
                "index": index,
                "id": id,
                "error": str(e),
            },
        )
        raise


async def search_documents(
    index: str,
    query: Dict[str, Any],
    size: int = 10,
    from_: int = 0,
) -> List[Dict[str, Any]]:
    """Search documents in Elasticsearch."""
    try:
        response = await es_client.search(
            index=index,
            body=query,
            size=size,
            from_=from_,
        )
        return [hit["_source"] for hit in response["hits"]["hits"]]
    except Exception as e:
        logger.error(
            "Failed to search documents",
            extra={
                "index": index,
                "error": str(e),
            },
        )
        raise


async def delete_document(index: str, id: str) -> bool:
    """Delete a document from Elasticsearch."""
    try:
        await es_client.delete(
            index=index,
            id=id,
        )
        logger.debug(
            "Document deleted",
            extra={
                "index": index,
                "id": id,
            },
        )
        return True
    except NotFoundError:
        return False
    except Exception as e:
        logger.error(
            "Failed to delete document",
            extra={
                "index": index,
                "id": id,
                "error": str(e),
            },
        )
        raise


async def close_connection() -> None:
    """Close Elasticsearch connection."""
    await es_client.close() 