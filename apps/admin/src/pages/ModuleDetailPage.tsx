import React, { useEffect, useState } from 'react';
import { useNavigate, useParams } from 'react-router-dom';
import { LessonList } from '../components/Course/LessonList';
import { LessonForm } from '../components/Course/LessonForm';

interface Module {
  id: string;
  title: string;
  description: string;
  order: number;
  courseId: string;
  createdAt: string;
  updatedAt: string;
}

interface Lesson {
  id: string;
  title: string;
  description: string;
  content: string;
  order: number;
  duration: number;
  moduleId: string;
  createdAt: string;
  updatedAt: string;
}

export const ModuleDetailPage: React.FC = () => {
  const { moduleId } = useParams<{ moduleId: string }>();
  const navigate = useNavigate();
  const [module, setModule] = useState<Module | null>(null);
  const [lessons, setLessons] = useState<Lesson[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [showLessonForm, setShowLessonForm] = useState(false);

  useEffect(() => {
    const fetchModuleAndLessons = async () => {
      try {
        const [moduleResponse, lessonsResponse] = await Promise.all([
          fetch(`/api/modules/${moduleId}`),
          fetch(`/api/modules/${moduleId}/lessons`),
        ]);

        if (!moduleResponse.ok || !lessonsResponse.ok) {
          throw new Error('Failed to fetch module data');
        }

        const moduleData = await moduleResponse.json();
        const lessonsData = await lessonsResponse.json();

        setModule(moduleData);
        setLessons(lessonsData);
      } catch (err) {
        setError(err instanceof Error ? err.message : 'An error occurred');
      } finally {
        setLoading(false);
      }
    };

    if (moduleId) {
      fetchModuleAndLessons();
    }
  }, [moduleId]);

  const handleDeleteLesson = async (lessonId: string) => {
    try {
      const response = await fetch(`/api/lessons/${lessonId}`, {
        method: 'DELETE',
      });

      if (!response.ok) {
        throw new Error('Failed to delete lesson');
      }

      setLessons(lessons.filter((lesson) => lesson.id !== lessonId));
    } catch (err) {
      setError(err instanceof Error ? err.message : 'An error occurred');
    }
  };

  const handleCreateLesson = async (data: {
    title: string;
    description: string;
    content: string;
    order: number;
    duration: number;
  }) => {
    try {
      const response = await fetch(`/api/modules/${moduleId}/lessons`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
      });

      if (!response.ok) {
        throw new Error('Failed to create lesson');
      }

      const newLesson = await response.json();
      setLessons([...lessons, newLesson]);
      setShowLessonForm(false);
    } catch (err) {
      setError(err instanceof Error ? err.message : 'An error occurred');
    }
  };

  if (loading) {
    return (
      <div className="flex justify-center items-center h-64">
        <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-500"></div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="text-center py-8">
        <p className="text-red-500">{error}</p>
      </div>
    );
  }

  if (!module) {
    return (
      <div className="text-center py-8">
        <p className="text-gray-500">Module not found</p>
      </div>
    );
  }

  return (
    <div className="container mx-auto px-4 py-8">
      <div className="flex justify-between items-center mb-8">
        <div>
          <h1 className="text-3xl font-bold text-gray-900">{module.title}</h1>
          <p className="text-gray-600 mt-2">{module.description}</p>
        </div>
        <div className="space-x-4">
          <button
            onClick={() => navigate(`/modules/${moduleId}/edit`)}
            className="bg-blue-600 hover:bg-blue-700 text-white font-medium py-2 px-4 rounded-md"
          >
            Edit Module
          </button>
          <button
            onClick={() => setShowLessonForm(true)}
            className="bg-green-600 hover:bg-green-700 text-white font-medium py-2 px-4 rounded-md"
          >
            Add Lesson
          </button>
        </div>
      </div>

      {error && (
        <div className="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded mb-4">
          {error}
        </div>
      )}

      {showLessonForm && (
        <div className="mb-8">
          <h2 className="text-2xl font-bold text-gray-900 mb-4">Create New Lesson</h2>
          <LessonForm moduleId={moduleId} onSubmit={handleCreateLesson} />
        </div>
      )}

      <div>
        <h2 className="text-2xl font-bold text-gray-900 mb-4">Lessons</h2>
        <LessonList
          lessons={lessons}
          onDelete={handleDeleteLesson}
          onEdit={(lessonId) => navigate(`/lessons/${lessonId}/edit`)}
        />
      </div>
    </div>
  );
}; 