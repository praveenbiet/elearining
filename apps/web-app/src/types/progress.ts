export interface LessonProgress {
  lessonId: string;
  completed: boolean;
  lastPosition?: number;
  completedAt?: string;
}

export interface ModuleProgress {
  moduleId: string;
  completed: boolean;
  completedAt?: string;
  lessons: LessonProgress[];
}

export interface CourseProgress {
  courseId: string;
  completed: boolean;
  completedAt?: string;
  lastAccessedAt: string;
  modules: ModuleProgress[];
  currentLessonId?: string;
  currentModuleId?: string;
} 