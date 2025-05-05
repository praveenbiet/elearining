import React from 'react';
import { useParams } from 'react-router-dom';

interface Module {
  id: string;
  title: string;
  description: string;
  order: number;
  lessons: Lesson[];
}

interface Lesson {
  id: string;
  title: string;
  description: string;
  content: string;
  order: number;
  duration: number;
}

interface CourseDetailProps {
  id: string;
  title: string;
  description: string;
  instructorName: string;
  level: string;
  duration: number;
  price: number;
  thumbnailUrl?: string;
  modules: Module[];
}

export const CourseDetail: React.FC<CourseDetailProps> = ({
  id,
  title,
  description,
  instructorName,
  level,
  duration,
  price,
  thumbnailUrl,
  modules,
}) => {
  const { courseId } = useParams<{ courseId: string }>();

  return (
    <div className="max-w-4xl mx-auto py-8">
      <div className="bg-white rounded-lg shadow-lg overflow-hidden">
        {thumbnailUrl && (
          <img
            src={thumbnailUrl}
            alt={title}
            className="w-full h-64 object-cover"
          />
        )}
        <div className="p-6">
          <h1 className="text-3xl font-bold text-gray-900 mb-4">{title}</h1>
          <p className="text-gray-600 mb-6">{description}</p>
          <div className="flex items-center justify-between mb-6">
            <div className="flex items-center space-x-4">
              <span className="text-gray-500">Instructor: {instructorName}</span>
              <span className="text-gray-500 capitalize">Level: {level}</span>
            </div>
            <div className="flex items-center space-x-4">
              <span className="text-gray-500">{duration} minutes</span>
              <span className="text-2xl font-bold text-blue-600">
                ${(price / 100).toFixed(2)}
              </span>
            </div>
          </div>
          <div className="space-y-6">
            {modules.map((module) => (
              <div key={module.id} className="border rounded-lg p-4">
                <h2 className="text-xl font-semibold mb-2">{module.title}</h2>
                <p className="text-gray-600 mb-4">{module.description}</p>
                <div className="space-y-4">
                  {module.lessons.map((lesson) => (
                    <div key={lesson.id} className="pl-4 border-l-2 border-blue-200">
                      <h3 className="text-lg font-medium">{lesson.title}</h3>
                      <p className="text-gray-600 text-sm">{lesson.description}</p>
                      <div className="flex items-center justify-between mt-2">
                        <span className="text-gray-500 text-sm">
                          {lesson.duration} minutes
                        </span>
                        <button className="text-blue-600 hover:text-blue-800">
                          Start Lesson
                        </button>
                      </div>
                    </div>
                  ))}
                </div>
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
}; 