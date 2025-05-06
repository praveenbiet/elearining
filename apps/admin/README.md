# Admin App

This is the admin application for managing courses, modules, and lessons in the e-learning platform.

## Features

- Create, edit, and delete courses
- Create, edit, and delete modules within courses
- Create, edit, and delete lessons within modules
- View course, module, and lesson details
- Responsive design with Tailwind CSS

## Getting Started

### Prerequisites

- Node.js (v14 or later)
- npm or yarn

### Installation

1. Install dependencies:
   ```bash
   npm install
   # or
   yarn install
   ```

2. Start the development server:
   ```bash
   npm start
   # or
   yarn start
   ```

3. Open [http://localhost:3000](http://localhost:3000) to view the app in your browser.

## Development

The app is built with:

- React 18
- TypeScript
- React Router v6
- Tailwind CSS
- ESLint and Prettier for code quality

## Project Structure

```
src/
  ├── components/
  │   └── Course/
  │       ├── CourseForm.tsx
  │       ├── CourseList.tsx
  │       ├── ModuleForm.tsx
  │       ├── ModuleList.tsx
  │       ├── LessonForm.tsx
  │       └── LessonList.tsx
  ├── pages/
  │   ├── CourseListPage.tsx
  │   ├── CreateCoursePage.tsx
  │   ├── EditCoursePage.tsx
  │   ├── CourseDetailPage.tsx
  │   ├── ModuleDetailPage.tsx
  │   └── LessonDetailPage.tsx
  ├── App.tsx
  ├── index.tsx
  └── index.css
```

## API Integration

The app communicates with the backend API using the following endpoints:

- Courses: `/api/courses`
- Modules: `/api/modules`
- Lessons: `/api/lessons`

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License. 