import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { CourseListPage } from './pages/CourseListPage';
import { CourseDetailPage } from './pages/CourseDetailPage';
import { CreateCoursePage } from './pages/CreateCoursePage';
import { EditCoursePage } from './pages/EditCoursePage';
import { CreateModulePage } from './pages/CreateModulePage';
import { EditModulePage } from './pages/EditModulePage';
import { CreateLessonPage } from './pages/CreateLessonPage';
import { EditLessonPage } from './pages/EditLessonPage';

export const App: React.FC = () => {
  return (
    <Router>
      <div className="min-h-screen bg-gray-100">
        <nav className="bg-white shadow-sm">
          <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div className="flex justify-between h-16">
              <div className="flex">
                <div className="flex-shrink-0 flex items-center">
                  <h1 className="text-xl font-bold text-gray-900">
                    E-Learning Admin
                  </h1>
                </div>
              </div>
            </div>
          </div>
        </nav>
        <div className="py-6">
          <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <Routes>
              <Route path="/" element={<CourseListPage />} />
              <Route path="/courses/new" element={<CreateCoursePage />} />
              <Route path="/courses/:courseId" element={<CourseDetailPage />} />
              <Route path="/courses/:courseId/edit" element={<EditCoursePage />} />
              <Route
                path="/courses/:courseId/modules/new"
                element={<CreateModulePage />}
              />
              <Route
                path="/courses/:courseId/modules/:moduleId/edit"
                element={<EditModulePage />}
              />
              <Route
                path="/courses/:courseId/modules/:moduleId/lessons/new"
                element={<CreateLessonPage />}
              />
              <Route
                path="/courses/:courseId/modules/:moduleId/lessons/:lessonId/edit"
                element={<EditLessonPage />}
              />
            </Routes>
          </div>
        </div>
      </div>
    </Router>
  );
}; 