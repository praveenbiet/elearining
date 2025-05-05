import React, { useState } from 'react';
import { useNavigate, useParams } from 'react-router-dom';
import { ModuleForm } from '../components/Course/ModuleForm';

interface ModuleFormData {
  title: string;
  description: string;
  order: number;
}

export const CreateModulePage: React.FC = () => {
  const { courseId } = useParams<{ courseId: string }>();
  const navigate = useNavigate();
  const [error, setError] = useState<string | null>(null);

  const handleSubmit = async (data: ModuleFormData) => {
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

      navigate(`/courses/${courseId}`);
    } catch (err) {
      setError(err instanceof Error ? err.message : 'An error occurred');
    }
  };

  return (
    <div className="container mx-auto px-4 py-8">
      <h1 className="text-3xl font-bold text-gray-900 mb-8">Create New Module</h1>
      {error && (
        <div className="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded mb-4">
          {error}
        </div>
      )}
      <ModuleForm courseId={courseId!} onSubmit={handleSubmit} />
    </div>
  );
}; 