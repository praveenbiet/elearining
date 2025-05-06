/**
 * Application constants used throughout the app
 */

// Pagination defaults
export const DEFAULT_PAGE_SIZE = 10;
export const DEFAULT_PAGE_NUMBER = 1;

// UI constants
export const DEBOUNCE_DELAY = 300; // ms
export const NOTIFICATION_TIMEOUT = 5000; // ms

// Form validation
export const VALIDATION = {
  PASSWORD_MIN_LENGTH: 8,
  NAME_MIN_LENGTH: 2,
  NAME_MAX_LENGTH: 50,
  EMAIL_REGEX: /^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}$/i,
};

// Course difficulties
export const COURSE_DIFFICULTIES = [
  'beginner',
  'intermediate',
  'advanced',
] as const;

// User roles
export const USER_ROLES = [
  'student',
  'instructor',
  'admin',
] as const;

// Local storage keys
export const STORAGE_KEYS = {
  AUTH_TOKEN: 'auth_token',
  USER_INFO: 'user_info',
  THEME: 'theme_preference',
};

// Routes that don't require authentication
export const PUBLIC_ROUTES = [
  '/',
  '/login',
  '/register',
  '/forgot-password',
  '/reset-password',
  '/browse-courses',
];

// Routes that require specific roles
export const INSTRUCTOR_ROUTES = [
  '/instructor-dashboard',
  '/create-course',
  '/manage-courses',
];

export const ADMIN_ROUTES = [
  '/admin',
  '/admin/users',
  '/admin/courses',
  '/admin/settings',
];

// Export all constants as default
export default {
  DEFAULT_PAGE_SIZE,
  DEFAULT_PAGE_NUMBER,
  DEBOUNCE_DELAY,
  NOTIFICATION_TIMEOUT,
  VALIDATION,
  COURSE_DIFFICULTIES,
  USER_ROLES,
  STORAGE_KEYS,
  PUBLIC_ROUTES,
  INSTRUCTOR_ROUTES,
  ADMIN_ROUTES,
}; 