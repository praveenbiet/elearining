/**
 * Application configuration that processes environment variables
 * with sensible defaults for local development
 */

// Define the shape of our app config
interface AppConfig {
  // API configuration
  API_URL: string;
  API_TIMEOUT: number;
  
  // Feature flags
  ENABLE_ANALYTICS: boolean;
  ENABLE_NOTIFICATIONS: boolean;
  ENABLE_DISCUSSIONS: boolean;
  
  // Other configs
  APP_NAME: string;
  SUPPORT_EMAIL: string;
  MAX_UPLOAD_SIZE: number; // in bytes
  ENVIRONMENT: 'development' | 'staging' | 'production';
}

// Create and export the config object
export const appConfig: AppConfig = {
  // API config - Use environment variables with fallbacks
  API_URL: process.env.REACT_APP_API_URL || 'http://localhost:8000/api/v1',
  API_TIMEOUT: Number(process.env.REACT_APP_API_TIMEOUT || 30000),
  
  // Feature flags - Default all to true in development, read from env in production
  ENABLE_ANALYTICS: process.env.REACT_APP_ENABLE_ANALYTICS !== 'false',
  ENABLE_NOTIFICATIONS: process.env.REACT_APP_ENABLE_NOTIFICATIONS !== 'false',
  ENABLE_DISCUSSIONS: process.env.REACT_APP_ENABLE_DISCUSSIONS !== 'false',
  
  // App details
  APP_NAME: process.env.REACT_APP_NAME || 'Learning Platform',
  SUPPORT_EMAIL: process.env.REACT_APP_SUPPORT_EMAIL || 'support@example.com',
  MAX_UPLOAD_SIZE: Number(process.env.REACT_APP_MAX_UPLOAD_SIZE || 50 * 1024 * 1024), // 50MB default
  
  // Environment
  ENVIRONMENT: (process.env.NODE_ENV as 'development' | 'staging' | 'production') || 'development',
};

// Helper function to check if we're in production
export const isProduction = appConfig.ENVIRONMENT === 'production';

// Helper function to check if we're in development
export const isDevelopment = appConfig.ENVIRONMENT === 'development'; 