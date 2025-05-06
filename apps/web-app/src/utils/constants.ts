export const COURSE_CATEGORIES = [
  'Web Development',
  'Mobile Development',
  'Data Science',
  'Artificial Intelligence',
  'Design',
  'Business',
] as const;

export const COURSE_LEVELS = [
  'Beginner',
  'Intermediate',
  'Advanced',
] as const;

export const SORT_OPTIONS = [
  { value: 'popularity', label: 'Most Popular' },
  { value: 'newest', label: 'Newest' },
  { value: 'highest-rated', label: 'Highest Rated' },
  { value: 'price-low', label: 'Price: Low to High' },
  { value: 'price-high', label: 'Price: High to Low' },
] as const;

export const DURATION_FILTERS = [
  { value: '0-2', label: '0-2 hours' },
  { value: '2-5', label: '2-5 hours' },
  { value: '5-10', label: '5-10 hours' },
  { value: '10+', label: '10+ hours' },
] as const; 