import React, { useState } from 'react';
import { useNavigate, useParams } from 'react-router-dom';
import { LessonForm } from '../components/Course/LessonForm';

interface LessonFormData {
  title: string;
  description: string;
  content: string;
  order: number;
  duration: number;
}

export const CreateLessonPage: React.FC = () => {
  const { courseId, moduleId } = useParams<{ courseId: string; moduleId: string }>();
  const navigate = useNavigate();
  const [error, setError] = useState<string | null>(null);

  const handleSubmit = async (data: LessonFormData) => {
    try {
      const response = await fetch(`/api/courses/modules/${moduleId}/lessons`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
      });

      if (!response.ok) {
        throw new Error('Failed to create lesson');
      }

      navigate(`/courses/${courseId}`);
    } catch (err) {
      setError(err instanceof Error ? err.message : 'An error occurred');
    }
  };

  return (
    <div className="container mx-auto px-4 py-8">
      <h1 className="text-3xl font-bold text-gray-900 mb-8">Create New Lesson</h1>
      {error && (
        <div className="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded mb-4">
          {error}
        </div>
      )}
      <LessonForm moduleId={moduleId!} onSubmit={handleSubmit} />
    </div>
  );
}; 