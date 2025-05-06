import React from 'react';
import { Outlet } from 'react-router-dom';
import { useSelector } from 'react-redux';

import Header from './Header';
import Sidebar from './Sidebar';
import { LoadingOverlay, NotificationDisplay } from '..';
import { RootState } from '../../../app/store';

const AppLayout: React.FC = () => {
  const { isLoading } = useSelector((state: RootState) => state.ui);

  return (
    <div className="min-h-screen flex flex-col bg-gray-50">
      <Header />
      <div className="flex flex-1">
        <Sidebar />
        <main className="flex-1 p-6 overflow-y-auto">
          {isLoading && <LoadingOverlay />}
          <NotificationDisplay />
          <Outlet />
        </main>
      </div>
    </div>
  );
};

export default AppLayout; 