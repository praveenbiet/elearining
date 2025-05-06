// API cache tag types
export const apiTags = [
  'User',
  'Course',
  'Lesson',
  'Module',
  'Progress',
  'Assessment',
  'Discussion',
  'Path',
  'Subscription',
  'Search',
  'Recommendation',
] as const;

// Union type of all cache tags
export type ApiTag = typeof apiTags[number]; 