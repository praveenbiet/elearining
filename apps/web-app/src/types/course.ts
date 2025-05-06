export interface Instructor {
  id: string;
  name: string;
  avatarUrl: string;
  bio: string;
}

export interface Module {
  id: string;
  title: string;
  description: string;
  order: number;
  lessons: Lesson[];
}

export interface Lesson {
  id: string;
  title: string;
  description: string;
  videoUrl: string;
  duration: number;
  order: number;
}

export interface Course {
  id: string;
  title: string;
  description: string;
  thumbnailUrl: string;
  category: string;
  level: 'beginner' | 'intermediate' | 'advanced';
  duration: number;
  rating: number;
  instructor: Instructor;
  modules: Module[];
  price: number;
  isPublished: boolean;
  createdAt: string;
  updatedAt: string;
} 