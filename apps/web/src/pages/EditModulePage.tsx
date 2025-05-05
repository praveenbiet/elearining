import React, { useEffect, useState } from 'react';
import { useNavigate, useParams } from 'react-router-dom';
import { ModuleForm } from '../components/Course/ModuleForm';

interface ModuleFormData {
  title: string;
  description: string;
  order: number;
}

interface Module extends ModuleFormData {
  id: string;
  courseId: string;
}

export const EditModulePage: React.FC = () => {
  const { courseId, moduleId } = useParams<{ courseId: string; moduleId: string }>();
  const navigate = useNavigate();
  const [module, setModule] = useState<Module | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const fetchModule = async () => {
      try {
        const response = await fetch(`/api/courses/modules/${moduleId}`);
        if (!response.ok) {
          throw new Error('Failed to fetch module');
        }
        const data = await response.json();
        setModule(data);
      } catch (err) {
        setError(err instanceof Error ? err.message : 'An error occurred');
      } finally {
        setLoading(false);
      }
    };

    if (moduleId) {
      fetchModule();
    }
  }, [moduleId]);

  const handleSubmit = async (data: ModuleFormData) => {
    try {
      const response = await fetch(`/api/courses/modules/${moduleId}`, {
        method: 'PUT',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
      });

      if (!response.ok) {
        throw new Error('Failed to update module');
      }

      navigate(`/courses/${courseId}`);
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
      <h1 className="text-3xl font-bold text-gray-900 mb-8">Edit Module</h1>
      {error && (
        <div className="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded mb-4">
          {error}
        </div>
      )}
      <ModuleForm
        courseId={courseId!}
        initialData={{
          title: module.title,
          description: module.description,
          order: module.order,
        }}
        onSubmit={handleSubmit}
      />
    </div>
  );
}; 