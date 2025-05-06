import React from 'react';
import { Course } from '../../types/course';

interface CourseSidebarProps {
  course: Course;
}

const CourseSidebar: React.FC<CourseSidebarProps> = ({ course }) => {
  return (
    <div className="space-y-6">
      <div className="bg-white rounded-lg shadow-sm p-6">
        <div className="aspect-w-16 aspect-h-9 mb-4">
          <img
            src={course.thumbnailUrl}
            alt={course.title}
            className="rounded-lg object-cover"
          />
        </div>
        
        <div className="flex items-center justify-between mb-4">
          <span className="text-2xl font-bold">${course.price}</span>
          <button className="btn btn-primary">Enroll Now</button>
        </div>
        
        <div className="space-y-4">
          <div className="flex items-center justify-between">
            <span className="text-gray-600">Duration</span>
            <span className="font-medium">{course.duration} hours</span>
          </div>
          
          <div className="flex items-center justify-between">
            <span className="text-gray-600">Level</span>
            <span className="font-medium capitalize">{course.level}</span>
          </div>
          
          <div className="flex items-center justify-between">
            <span className="text-gray-600">Category</span>
            <span className="font-medium">{course.category}</span>
          </div>
          
          <div className="flex items-center justify-between">
            <span className="text-gray-600">Rating</span>
            <div className="flex items-center">
              <svg className="w-4 h-4 text-yellow-400 mr-1" fill="currentColor" viewBox="0 0 20 20">
                <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z" />
              </svg>
              <span className="font-medium">{course.rating.toFixed(1)}</span>
            </div>
          </div>
        </div>
      </div>
      
      <div className="bg-white rounded-lg shadow-sm p-6">
        <h3 className="text-lg font-semibold mb-4">Instructor</h3>
        <div className="flex items-center">
          <img
            src={course.instructor.avatarUrl}
            alt={course.instructor.name}
            className="w-12 h-12 rounded-full mr-4"
          />
          <div>
            <h4 className="font-medium">{course.instructor.name}</h4>
            <p className="text-sm text-gray-600">{course.instructor.bio}</p>
          </div>
        </div>
      </div>
    </div>
  );
};

export default CourseSidebar; 