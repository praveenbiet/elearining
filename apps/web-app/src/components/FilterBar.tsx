import React from 'react';

interface FilterBarProps {
  filters: {
    category: string;
    level: string;
    duration: string;
    sortBy: string;
  };
  onChange: (filters: {
    category: string;
    level: string;
    duration: string;
    sortBy: string;
  }) => void;
}

const FilterBar: React.FC<FilterBarProps> = ({ filters, onChange }) => {
  const handleChange = (key: keyof typeof filters, value: string) => {
    onChange({
      ...filters,
      [key]: value,
    });
  };

  return (
    <div className="flex flex-wrap gap-4">
      <select
        value={filters.category}
        onChange={(e) => handleChange('category', e.target.value)}
        className="input"
      >
        <option value="">All Categories</option>
        <option value="web">Web Development</option>
        <option value="mobile">Mobile Development</option>
        <option value="data">Data Science</option>
        <option value="ai">Artificial Intelligence</option>
        <option value="design">Design</option>
        <option value="business">Business</option>
      </select>

      <select
        value={filters.level}
        onChange={(e) => handleChange('level', e.target.value)}
        className="input"
      >
        <option value="">All Levels</option>
        <option value="beginner">Beginner</option>
        <option value="intermediate">Intermediate</option>
        <option value="advanced">Advanced</option>
      </select>

      <select
        value={filters.duration}
        onChange={(e) => handleChange('duration', e.target.value)}
        className="input"
      >
        <option value="">Any Duration</option>
        <option value="0-2">0-2 hours</option>
        <option value="2-5">2-5 hours</option>
        <option value="5-10">5-10 hours</option>
        <option value="10+">10+ hours</option>
      </select>

      <select
        value={filters.sortBy}
        onChange={(e) => handleChange('sortBy', e.target.value)}
        className="input"
      >
        <option value="popularity">Most Popular</option>
        <option value="newest">Newest</option>
        <option value="highest-rated">Highest Rated</option>
        <option value="price-low">Price: Low to High</option>
        <option value="price-high">Price: High to Low</option>
      </select>
    </div>
  );
};

export default FilterBar; 