import React, { useEffect, useState } from 'react';
import { useNavigate, useParams } from 'react-router-dom';
import { ModuleList } from '../components/Course/ModuleList';
import { ModuleForm } from '../components/Course/ModuleForm';

interface Course {
  id: string;
  title: string;
  description: string;
  instructorName: string;
  level: string;
  duration: number;
  price: number;
  isPublished: boolean;
  createdAt: string;
  updatedAt: string;
}

interface Module {
  id: string;
  title: string;
  description: string;
  order: number;
  courseId: string;
  createdAt: string;
  updatedAt: string;
}

export const CourseDetailPage: React.FC = () => {
  const { courseId } = useParams<{ courseId: string }>();
  const navigate = useNavigate();
  const [course, setCourse] = useState<Course | null>(null);
  const [modules, setModules] = useState<Module[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [showModuleForm, setShowModuleForm] = useState(false);

  useEffect(() => {
    const fetchCourseAndModules = async () => {
      try {
        const [courseResponse, modulesResponse] = await Promise.all([
          fetch(`/api/courses/${courseId}`),
          fetch(`/api/courses/${courseId}/modules`),
        ]);

        if (!courseResponse.ok || !modulesResponse.ok) {
          throw new Error('Failed to fetch course data');
        }

        const courseData = await courseResponse.json();
        const modulesData = await modulesResponse.json();

        setCourse(courseData);
        setModules(modulesData);
      } catch (err) {
        setError(err instanceof Error ? err.message : 'An error occurred');
      } finally {
        setLoading(false);
      }
    };

    if (courseId) {
      fetchCourseAndModules();
    }
  }, [courseId]);

  const handleDeleteModule = async (moduleId: string) => {
    try {
      const response = await fetch(`/api/modules/${moduleId}`, {
        method: 'DELETE',
      });

      if (!response.ok) {
        throw new Error('Failed to delete module');
      }

      setModules(modules.filter((module) => module.id !== moduleId));
    } catch (err) {
      setError(err instanceof Error ? err.message : 'An error occurred');
    }
  };

  const handleCreateModule = async (data: {
    title: string;
    description: string;
    order: number;
  }) => {
    try {
      const response = await fetch(`/api/courses/${courseId}/modules`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
      });

      if (!response.ok) {
        throw new Error('Failed to create module');
      }

      const newModule = await response.json();
      setModules([...modules, newModule]);
      setShowModuleForm(false);
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

  if (!course) {
    return (
      <div className="text-center py-8">
        <p className="text-gray-500">Course not found</p>
      </div>
    );
  }

  return (
    <div className="container mx-auto px-4 py-8">
      <div className="flex justify-between items-center mb-8">
        <div>
          <h1 className="text-3xl font-bold text-gray-900">{course.title}</h1>
          <p className="text-gray-600 mt-2">{course.description}</p>
        </div>
        <div className="space-x-4">
          <button
            onClick={() => navigate(`/courses/${courseId}/edit`)}
            className="bg-blue-600 hover:bg-blue-700 text-white font-medium py-2 px-4 rounded-md"
          >
            Edit Course
          </button>
          <button
            onClick={() => setShowModuleForm(true)}
            className="bg-green-600 hover:bg-green-700 text-white font-medium py-2 px-4 rounded-md"
          >
            Add Module
          </button>
        </div>
      </div>

      {error && (
        <div className="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded mb-4">
          {error}
        </div>
      )}

      {showModuleForm && (
        <div className="mb-8">
          <h2 className="text-2xl font-bold text-gray-900 mb-4">Create New Module</h2>
          <ModuleForm courseId={courseId} onSubmit={handleCreateModule} />
        </div>
      )}

      <div>
        <h2 className="text-2xl font-bold text-gray-900 mb-4">Modules</h2>
        <ModuleList
          modules={modules}
          onDelete={handleDeleteModule}
          onEdit={(moduleId) => navigate(`/modules/${moduleId}/edit`)}
        />
      </div>
    </div>
  );
}; 