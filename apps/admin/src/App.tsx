import React from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import { CourseListPage } from './pages/CourseListPage';
import { CreateCoursePage } from './pages/CreateCoursePage';
import { EditCoursePage } from './pages/EditCoursePage';
import { CourseDetailPage } from './pages/CourseDetailPage';
import { ModuleDetailPage } from './pages/ModuleDetailPage';
import { LessonDetailPage } from './pages/LessonDetailPage';

export const App: React.FC = () => {
  return (
    <Router>
      <div className="min-h-screen bg-gray-100">
        <nav className="bg-white shadow-sm">
          <div className="container mx-auto px-4">
            <div className="flex justify-between h-16">
              <div className="flex">
                <div className="flex-shrink-0 flex items-center">
                  <Link to="/" className="text-xl font-bold text-gray-900">
                    Course Admin
                  </Link>
                </div>
                <div className="hidden sm:ml-6 sm:flex sm:space-x-8">
                  <Link
                    to="/"
                    className="border-transparent text-gray-500 hover:border-gray-300 hover:text-gray-700 inline-flex items-center px-1 pt-1 border-b-2 text-sm font-medium"
                  >
                    Courses
                  </Link>
                </div>
              </div>
            </div>
          </div>
        </nav>

        <main>
          <Routes>
            <Route path="/" element={<CourseListPage />} />
            <Route path="/courses/new" element={<CreateCoursePage />} />
            <Route path="/courses/:courseId" element={<CourseDetailPage />} />
            <Route path="/courses/:courseId/edit" element={<EditCoursePage />} />
            <Route path="/modules/:moduleId" element={<ModuleDetailPage />} />
            <Route path="/lessons/:lessonId" element={<LessonDetailPage />} />
          </Routes>
        </main>
      </div>
    </Router>
  );
}; 