import { api } from './index';
import { Course } from '../types/course';

interface GetCoursesParams {
  search?: string;
  category?: string;
  level?: string;
  duration?: string;
  sortBy?: string;
}

export const courseApi = api.injectEndpoints({
  endpoints: (builder) => ({
    getCourses: builder.query<Course[], GetCoursesParams>({
      query: (params) => ({
        url: '/courses',
        method: 'GET',
        params,
      }),
      providesTags: ['Course'],
    }),
    
    getCourseById: builder.query<Course, string>({
      query: (id) => ({
        url: `/courses/${id}`,
        method: 'GET',
      }),
      providesTags: (result, error, id) => [{ type: 'Course', id }],
    }),
    
    createCourse: builder.mutation<Course, Partial<Course>>({
      query: (course) => ({
        url: '/courses',
        method: 'POST',
        body: course,
      }),
      invalidatesTags: ['Course'],
    }),
    
    updateCourse: builder.mutation<Course, { id: string; course: Partial<Course> }>({
      query: ({ id, course }) => ({
        url: `/courses/${id}`,
        method: 'PUT',
        body: course,
      }),
      invalidatesTags: (result, error, { id }) => [{ type: 'Course', id }],
    }),
    
    deleteCourse: builder.mutation<void, string>({
      query: (id) => ({
        url: `/courses/${id}`,
        method: 'DELETE',
      }),
      invalidatesTags: ['Course'],
    }),
  }),
});

export const {
  useGetCoursesQuery,
  useGetCourseByIdQuery,
  useCreateCourseMutation,
  useUpdateCourseMutation,
  useDeleteCourseMutation,
} = courseApi; 