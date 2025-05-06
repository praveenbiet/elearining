import React from 'react';
import { Routes, Route } from 'react-router-dom';
import { QueryClient, QueryClientProvider } from '@tanstack/react-query';
import { Provider } from 'react-redux';
import { store } from './store';

// Pages
import { 
  HomePage,
  LoginPage, 
  RegisterPage,
  BrowseCoursesPage,
  CoursePlayerPage,
  LearningPathPage,
  SkillAssessmentPage,
  UserProfilePage,
  SubscriptionPage,
  NotFoundPage
} from './pages';

// App Layout
import { AppLayout } from './shared/ui';

// Auth
import { PrivateRoute } from './app/routing';

const queryClient = new QueryClient();

const App: React.FC = () => {
  return (
    <Provider store={store}>
      <QueryClientProvider client={queryClient}>
        <Routes>
          {/* Public routes */}
          <Route element={<AppLayout />}>
            <Route path="/" element={<HomePage />} />
            <Route path="/login" element={<LoginPage />} />
            <Route path="/register" element={<RegisterPage />} />
            <Route path="/browse-courses" element={<BrowseCoursesPage />} />
            
            {/* Protected routes */}
            <Route 
              path="/courses/:courseId" 
              element={
                <PrivateRoute>
                  <CoursePlayerPage />
                </PrivateRoute>
              } 
            />
            <Route 
              path="/courses/:courseId/lessons/:lessonId" 
              element={
                <PrivateRoute>
                  <CoursePlayerPage />
                </PrivateRoute>
              } 
            />
            <Route 
              path="/paths/:pathId" 
              element={
                <PrivateRoute>
                  <LearningPathPage />
                </PrivateRoute>
              } 
            />
            <Route 
              path="/assessments/:assessmentId" 
              element={
                <PrivateRoute>
                  <SkillAssessmentPage />
                </PrivateRoute>
              } 
            />
            <Route 
              path="/profile" 
              element={
                <PrivateRoute>
                  <UserProfilePage />
                </PrivateRoute>
              } 
            />
            <Route 
              path="/subscription" 
              element={
                <PrivateRoute>
                  <SubscriptionPage />
                </PrivateRoute>
              } 
            />
            
            {/* Catch-all / 404 route */}
            <Route path="*" element={<NotFoundPage />} />
          </Route>
        </Routes>
      </QueryClientProvider>
    </Provider>
  );
};

export default App; 