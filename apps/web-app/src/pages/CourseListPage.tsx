import React, { useState } from 'react';
import { useGetCoursesQuery } from '../api/courseApi';
import CourseCard from '../components/Course/CourseCard';
import SearchBar from '../components/SearchBar';
import FilterBar from '../components/FilterBar';

const CourseListPage: React.FC = () => {
  const [search, setSearch] = useState('');
  const [filters, setFilters] = useState({
    category: '',
    level: '',
    duration: '',
    sortBy: 'popularity',
  });

  const { data: courses, isLoading, error } = useGetCoursesQuery({
    search,
    ...filters,
  });

  if (isLoading) {
    return (
      <div className="flex justify-center items-center min-h-[400px]">
        <div className="animate-spin rounded-full h-12 w-12 border-t-2 border-b-2 border-primary-600"></div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="text-center py-8">
        <h2 className="text-2xl font-semibold text-red-600 mb-4">
          Error loading courses
        </h2>
        <p className="text-gray-600">
          Please try again later or contact support if the problem persists.
        </p>
      </div>
    );
  }

  return (
    <div className="container mx-auto px-4 py-8">
      <div className="mb-8">
        <h1 className="text-3xl font-bold mb-4">Browse Courses</h1>
        <div className="flex flex-col md:flex-row gap-4 mb-6">
          <SearchBar value={search} onChange={setSearch} />
          <FilterBar filters={filters} onChange={setFilters} />
        </div>
      </div>

      {courses && courses.length > 0 ? (
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">
          {courses.map((course) => (
            <CourseCard key={course.id} course={course} />
          ))}
        </div>
      ) : (
        <div className="text-center py-12">
          <h2 className="text-2xl font-semibold text-gray-800 mb-4">
            No courses found
          </h2>
          <p className="text-gray-600">
            Try adjusting your search or filter criteria
          </p>
        </div>
      )}
    </div>
  );
};

export default CourseListPage; 