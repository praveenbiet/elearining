import React from 'react';
import { Link } from 'react-router-dom';
import { Course } from '../../types/course';

interface CourseCardProps {
  course: Course;
}

const CourseCard: React.FC<CourseCardProps> = ({ course }) => {
  return (
    <Link to={`/courses/${course.id}`} className="block">
      <div className="bg-white rounded-lg shadow-sm overflow-hidden hover:shadow-md transition-shadow">
        <div className="aspect-w-16 aspect-h-9">
          <img
            src={course.thumbnailUrl}
            alt={course.title}
            className="object-cover"
          />
        </div>
        
        <div className="p-4">
          <div className="flex items-center space-x-2 mb-2">
            <span className="px-2 py-1 bg-primary-100 text-primary-600 rounded-full text-xs">
              {course.category}
            </span>
            <span className="px-2 py-1 bg-gray-100 text-gray-600 rounded-full text-xs">
              {course.level}
            </span>
          </div>
          
          <h3 className="text-lg font-semibold mb-2 line-clamp-2">{course.title}</h3>
          
          <p className="text-gray-600 text-sm mb-4 line-clamp-2">{course.description}</p>
          
          <div className="flex items-center justify-between">
            <div className="flex items-center">
              <img
                src={course.instructor.avatarUrl}
                alt={course.instructor.name}
                className="w-6 h-6 rounded-full mr-2"
              />
              <span className="text-sm text-gray-600">{course.instructor.name}</span>
            </div>
            
            <div className="flex items-center">
              <svg className="w-4 h-4 text-yellow-400 mr-1" fill="currentColor" viewBox="0 0 20 20">
                <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z" />
              </svg>
              <span className="text-sm font-medium">{course.rating.toFixed(1)}</span>
            </div>
          </div>
          
          <div className="mt-4 flex items-center justify-between">
            <span className="text-lg font-bold">${course.price}</span>
            <span className="text-sm text-gray-600">{course.duration} hours</span>
          </div>
        </div>
      </div>
    </Link>
  );
};

export default CourseCard; 