# Frontend Applications Overview

The E-Learning Platform has two main frontend applications: the user-facing web app and the admin portal. Both are built using React and follow a consistent architecture.

## Architecture

Both frontend applications follow a Feature-Sliced Design (FSD) architecture:

```
src/
├── app/              # App setup & providers
├── pages/            # Page components
├── features/         # Feature modules
├── shared/           # Shared code
├── entities/         # Entity types
├── styles/           # Global styles
├── assets/           # Static assets
└── i18n/             # Internationalization
```

## Technology Stack

- **Framework**: React
- **Language**: TypeScript
- **State Management**: Redux Toolkit + RTK Query
- **Styling**: Tailwind CSS
- **Routing**: React Router
- **Testing**: Jest + React Testing Library
- **E2E Testing**: Cypress
- **Build Tool**: Vite
- **Linting**: ESLint
- **Formatting**: Prettier

## Shared Libraries

The frontend applications share several libraries:

1. **Design System** - Reusable UI components
2. **Common Hooks** - Shared React hooks
3. **API Client** - Generated API client

## Web App

The main user-facing application with features like:

- Course browsing
- Video playback
- Learning path navigation
- Assessments
- User profile
- Progress tracking
- Search
- Recommendations
- Discussions
- Subscription management

## Admin Portal

The management interface with features like:

- User management
- Course management
- Video upload
- Analytics reporting
- Platform settings
- Subscription plan management

## State Management

- **Redux Toolkit** for global state
- **RTK Query** for API state
- **React Context** for local state
- **Local Storage** for persistence

## API Integration

- Generated API client from OpenAPI spec
- RTK Query for API state management
- Error handling middleware
- Request/response interceptors

## Styling Approach

- Tailwind CSS for utility-first styling
- CSS Modules for component-specific styles
- Design System for consistent UI
- Responsive design
- Dark mode support

## Testing Strategy

1. **Unit Tests** - Component testing
2. **Integration Tests** - Feature testing
3. **E2E Tests** - User flow testing
4. **Visual Tests** - Component snapshot testing

## Performance Optimization

1. **Code Splitting** - Route-based and component-based
2. **Lazy Loading** - Dynamic imports
3. **Caching** - API response caching
4. **Bundle Optimization** - Tree shaking
5. **Image Optimization** - Lazy loading and formats

## Accessibility

- WCAG 2.1 compliance
- ARIA attributes
- Keyboard navigation
- Screen reader support
- Color contrast
- Focus management

## Internationalization

- i18next for translations
- Language detection
- RTL support
- Date/number formatting
- Pluralization

## Development Workflow

1. **Feature Branches** - Git workflow
2. **Code Review** - Pull requests
3. **CI/CD** - Automated testing and deployment
4. **Version Control** - Semantic versioning

## Build and Deployment

- Vite for development and building
- Docker for containerization
- Kubernetes for orchestration
- CDN for static assets
- Environment-specific builds

## Monitoring

- Error tracking
- Performance monitoring
- User analytics
- Feature usage tracking

## Security

- XSS prevention
- CSRF protection
- Content Security Policy
- Secure headers
- Authentication handling

## Future Improvements

1. **Micro Frontends** - Potential future architecture
2. **Web Components** - Reusable components
3. **PWA Support** - Offline capabilities
4. **SSR/SSG** - Server-side rendering
5. **WebAssembly** - Performance optimization 