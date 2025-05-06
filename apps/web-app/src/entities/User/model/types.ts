/**
 * User entity types
 */

// Base user type
export interface User {
  id: string;
  email: string;
  name?: string;
  avatarUrl?: string;
  role: UserRole;
  createdAt: string; // ISO date string
  updatedAt: string; // ISO date string
}

// User roles
export type UserRole = 'student' | 'instructor' | 'admin';

// User profile details
export interface UserProfile extends User {
  bio?: string;
  location?: string;
  website?: string;
  company?: string;
  interests?: string[];
  skills?: string[];
  socialLinks?: {
    twitter?: string;
    linkedin?: string;
    github?: string;
    facebook?: string;
  };
}

// User progress in a course
export interface UserProgress {
  userId: string;
  courseId: string;
  progress: number; // Percentage 0-100
  lastAccessedAt: string; // ISO date string
  completedLessons: string[]; // Array of lesson IDs
  status: 'not-started' | 'in-progress' | 'completed';
}

// User subscription status
export interface UserSubscription {
  userId: string;
  planId: string;
  planName: string;
  startDate: string; // ISO date string
  endDate: string; // ISO date string
  status: 'active' | 'cancelled' | 'expired';
  features: string[]; // Array of feature identifiers the user has access to
}

// User authentication response
export interface AuthResponse {
  user: User;
  token: string;
} 