import React from 'react';
import { useParams } from 'react-router-dom';
import { useGetCourseByIdQuery } from '../api/courseApi';
import CourseContent from '../components/Course/CourseContent';
import CourseSidebar from '../components/Course/CourseSidebar';
import CourseHeader from '../components/Course/CourseHeader';

const CourseDetailPage: React.FC = () => {
  const { courseId } = useParams<{ courseId: string }>();
  const { data: course, isLoading, error } = useGetCourseByIdQuery(courseId || '');

  if (isLoading) {
    return (
      <div className="flex justify-center items-center min-h-[400px]">
        <div className="animate-spin rounded-full h-12 w-12 border-t-2 border-b-2 border-primary-600"></div>
      </div>
    );
  }

  if (error || !course) {
    return (
      <div className="text-center py-8">
        <h2 className="text-2xl font-semibold text-red-600 mb-4">
          Error loading course
        </h2>
        <p className="text-gray-600">
          Please try again later or contact support if the problem persists.
        </p>
      </div>
    );
  }

  return (
    <div className="space-y-8">
      <CourseHeader course={course} />
      
      <div className="container mx-auto px-4">
        <div className="flex flex-col lg:flex-row gap-8">
          <div className="lg:w-2/3">
            <CourseContent course={course} />
          </div>
          
          <div className="lg:w-1/3">
            <CourseSidebar course={course} />
          </div>
        </div>
      </div>
    </div>
  );
};

export default CourseDetailPage; 