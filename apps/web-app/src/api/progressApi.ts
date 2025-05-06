import { api } from './index';
import { CourseProgress, LessonProgress } from '../types/progress';

export const progressApi = api.injectEndpoints({
  endpoints: (builder) => ({
    getCourseProgress: builder.query<CourseProgress, string>({
      query: (courseId) => `/progress/courses/${courseId}`,
      providesTags: (result, error, courseId) => [{ type: 'Progress', id: courseId }],
    }),
    
    updateLessonProgress: builder.mutation<LessonProgress, { courseId: string; lessonId: string; progress: Partial<LessonProgress> }>({
      query: ({ courseId, lessonId, progress }) => ({
        url: `/progress/courses/${courseId}/lessons/${lessonId}`,
        method: 'PATCH',
        body: progress,
      }),
      invalidatesTags: (result, error, { courseId }) => [{ type: 'Progress', id: courseId }],
    }),
    
    getEnrolledCourses: builder.query<CourseProgress[], void>({
      query: () => '/progress/courses',
      providesTags: ['Progress'],
    }),
  }),
});

export const {
  useGetCourseProgressQuery,
  useUpdateLessonProgressMutation,
  useGetEnrolledCoursesQuery,
} = progressApi; 