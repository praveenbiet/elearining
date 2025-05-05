# Data Models Overview

The E-Learning Platform uses a relational database (PostgreSQL) with a well-defined data model. This document provides an overview of the main entities and their relationships.

## Core Entities

### User
```sql
CREATE TABLE users (
    id UUID PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    is_active BOOLEAN DEFAULT true,
    is_verified BOOLEAN DEFAULT false,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);
```

### User Profile
```sql
CREATE TABLE user_profiles (
    user_id UUID PRIMARY KEY REFERENCES users(id),
    bio TEXT,
    avatar_url VARCHAR(255),
    job_title VARCHAR(100),
    company VARCHAR(100),
    location VARCHAR(100),
    website VARCHAR(255),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);
```

### Course
```sql
CREATE TABLE courses (
    id UUID PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    slug VARCHAR(255) UNIQUE NOT NULL,
    thumbnail_url VARCHAR(255),
    author_id UUID REFERENCES users(id),
    status VARCHAR(50) DEFAULT 'draft',
    level VARCHAR(50),
    duration INTEGER, -- in minutes
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);
```

### Module
```sql
CREATE TABLE modules (
    id UUID PRIMARY KEY,
    course_id UUID REFERENCES courses(id),
    title VARCHAR(255) NOT NULL,
    description TEXT,
    order_index INTEGER NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);
```

### Lesson
```sql
CREATE TABLE lessons (
    id UUID PRIMARY KEY,
    module_id UUID REFERENCES modules(id),
    title VARCHAR(255) NOT NULL,
    description TEXT,
    video_asset_id UUID,
    duration INTEGER, -- in minutes
    order_index INTEGER NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);
```

### Video Asset
```sql
CREATE TABLE video_assets (
    id UUID PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    provider VARCHAR(50) NOT NULL,
    provider_id VARCHAR(255) NOT NULL,
    status VARCHAR(50) DEFAULT 'processing',
    duration INTEGER, -- in minutes
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);
```

### Assessment
```sql
CREATE TABLE assessments (
    id UUID PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    passing_score INTEGER,
    time_limit INTEGER, -- in minutes
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);
```

### Question
```sql
CREATE TABLE questions (
    id UUID PRIMARY KEY,
    assessment_id UUID REFERENCES assessments(id),
    text TEXT NOT NULL,
    type VARCHAR(50) NOT NULL,
    order_index INTEGER NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);
```

### Answer Option
```sql
CREATE TABLE answer_options (
    id UUID PRIMARY KEY,
    question_id UUID REFERENCES questions(id),
    text TEXT NOT NULL,
    is_correct BOOLEAN DEFAULT false,
    order_index INTEGER NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);
```

### Learning Path
```sql
CREATE TABLE learning_paths (
    id UUID PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    thumbnail_url VARCHAR(255),
    author_id UUID REFERENCES users(id),
    status VARCHAR(50) DEFAULT 'draft',
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);
```

### Path Step
```sql
CREATE TABLE path_steps (
    id UUID PRIMARY KEY,
    path_id UUID REFERENCES learning_paths(id),
    entity_type VARCHAR(50) NOT NULL, -- 'course' or 'assessment'
    entity_id UUID NOT NULL,
    order_index INTEGER NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);
```

### User Progress
```sql
CREATE TABLE user_progress (
    id UUID PRIMARY KEY,
    user_id UUID REFERENCES users(id),
    entity_type VARCHAR(50) NOT NULL, -- 'course', 'module', 'lesson', 'assessment'
    entity_id UUID NOT NULL,
    status VARCHAR(50) NOT NULL,
    progress_percentage INTEGER DEFAULT 0,
    completed_at TIMESTAMP WITH TIME ZONE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);
```

### Subscription
```sql
CREATE TABLE subscriptions (
    id UUID PRIMARY KEY,
    user_id UUID REFERENCES users(id),
    plan_id UUID REFERENCES subscription_plans(id),
    status VARCHAR(50) NOT NULL,
    start_date TIMESTAMP WITH TIME ZONE NOT NULL,
    end_date TIMESTAMP WITH TIME ZONE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);
```

### Subscription Plan
```sql
CREATE TABLE subscription_plans (
    id UUID PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    price DECIMAL(10,2) NOT NULL,
    billing_cycle VARCHAR(50) NOT NULL,
    features JSONB NOT NULL,
    is_active BOOLEAN DEFAULT true,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);
```

## Relationships

1. **User to User Profile**: One-to-One
2. **User to Course**: One-to-Many (Author)
3. **Course to Module**: One-to-Many
4. **Module to Lesson**: One-to-Many
5. **Lesson to Video Asset**: One-to-One
6. **Assessment to Question**: One-to-Many
7. **Question to Answer Option**: One-to-Many
8. **Learning Path to Path Step**: One-to-Many
9. **User to User Progress**: One-to-Many
10. **User to Subscription**: One-to-Many
11. **Subscription Plan to Subscription**: One-to-Many

## Indexes

Key indexes for performance optimization:

1. Users: email
2. Courses: slug, author_id
3. Modules: course_id, order_index
4. Lessons: module_id, order_index
5. User Progress: user_id, entity_type, entity_id
6. Subscriptions: user_id, status

## Data Access Patterns

1. **Repository Pattern** - Abstract data access
2. **Caching** - Redis for frequently accessed data
3. **Search** - Elasticsearch for full-text search
4. **Analytics** - Separate analytics database

## Data Migration Strategy

1. **Alembic** for schema migrations
2. **Data Migrations** for content updates
3. **Version Control** for migration scripts
4. **Rollback Plan** for failed migrations

## Data Security

1. **Encryption** - Sensitive data at rest
2. **Access Control** - Row-level security
3. **Audit Logging** - Data changes tracking
4. **Data Retention** - Archival policies

## Future Considerations

1. **Sharding** - Horizontal scaling
2. **Read Replicas** - Read performance
3. **Data Warehouse** - Analytics
4. **Caching Strategy** - Performance optimization
5. **Data Archival** - Storage optimization 