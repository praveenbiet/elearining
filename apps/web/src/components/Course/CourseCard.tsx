import React from 'react';
import { Link } from 'react-router-dom';

interface CourseCardProps {
  id: string;
  title: string;
  description: string;
  instructorName: string;
  level: string;
  duration: number;
  price: number;
  thumbnailUrl?: string;
}

export const CourseCard: React.FC<CourseCardProps> = ({
  id,
  title,
  description,
  instructorName,
  level,
  duration,
  price,
  thumbnailUrl,
}) => {
  return (
    <Link to={`/courses/${id}`} className="block">
      <div className="bg-white rounded-lg shadow-md overflow-hidden hover:shadow-lg transition-shadow">
        {thumbnailUrl && (
          <img
            src={thumbnailUrl}
            alt={title}
            className="w-full h-48 object-cover"
          />
        )}
        <div className="p-4">
          <h3 className="text-xl font-semibold text-gray-900 mb-2">{title}</h3>
          <p className="text-gray-600 text-sm mb-4 line-clamp-2">{description}</p>
          <div className="flex items-center justify-between text-sm text-gray-500">
            <span>{instructorName}</span>
            <span className="capitalize">{level}</span>
          </div>
          <div className="flex items-center justify-between mt-2">
            <span className="text-gray-500 text-sm">{duration} minutes</span>
            <span className="text-lg font-semibold text-blue-600">
              ${(price / 100).toFixed(2)}
            </span>
          </div>
        </div>
      </div>
    </Link>
  );
}; 