import React from 'react';
import { Course } from '../../types/course';

interface CourseHeaderProps {
  course: Course;
}

const CourseHeader: React.FC<CourseHeaderProps> = ({ course }) => {
  return (
    <div className="bg-gray-900 text-white py-12">
      <div className="container mx-auto px-4">
        <div className="max-w-3xl">
          <div className="flex items-center space-x-2 mb-4">
            <span className="px-3 py-1 bg-primary-600 rounded-full text-sm">
              {course.category}
            </span>
            <span className="px-3 py-1 bg-gray-700 rounded-full text-sm">
              {course.level}
            </span>
          </div>
          
          <h1 className="text-4xl font-bold mb-4">{course.title}</h1>
          
          <p className="text-xl text-gray-300 mb-6">{course.description}</p>
          
          <div className="flex items-center space-x-6">
            <div className="flex items-center">
              <img
                src={course.instructor.avatarUrl}
                alt={course.instructor.name}
                className="w-10 h-10 rounded-full mr-3"
              />
              <div>
                <p className="text-sm text-gray-400">Instructor</p>
                <p className="font-medium">{course.instructor.name}</p>
              </div>
            </div>
            
            <div>
              <p className="text-sm text-gray-400">Duration</p>
              <p className="font-medium">{course.duration} hours</p>
            </div>
            
            <div>
              <p className="text-sm text-gray-400">Rating</p>
              <div className="flex items-center">
                <svg className="w-4 h-4 text-yellow-400 mr-1" fill="currentColor" viewBox="0 0 20 20">
                  <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z" />
                </svg>
                <span className="font-medium">{course.rating.toFixed(1)}</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default CourseHeader; 