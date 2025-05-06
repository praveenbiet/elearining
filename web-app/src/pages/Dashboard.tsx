import React from 'react';
import { useSelector } from 'react-redux';
import {
  Container,
  Typography,
  Grid,
  Card,
  CardContent,
  CardActions,
  Button,
  Box,
} from '@mui/material';
import { RootState } from '../store';

const Dashboard: React.FC = () => {
  const { user } = useSelector((state: RootState) => state.auth);

  // Mock data for courses
  const enrolledCourses = [
    {
      id: 1,
      title: 'Introduction to React',
      progress: 75,
      lastAccessed: '2023-05-01',
    },
    {
      id: 2,
      title: 'Advanced TypeScript',
      progress: 30,
      lastAccessed: '2023-05-05',
    },
    {
      id: 3,
      title: 'Node.js Backend Development',
      progress: 10,
      lastAccessed: '2023-05-10',
    },
  ];

  return (
    <Container maxWidth="lg">
      <Box sx={{ mt: 4, mb: 4 }}>
        <Typography variant="h4" gutterBottom>
          Welcome back, {user?.name}!
        </Typography>
        <Typography variant="subtitle1" color="text.secondary">
          Continue your learning journey
        </Typography>
      </Box>

      <Grid container spacing={4}>
        {enrolledCourses.map((course) => (
          <Grid item xs={12} sm={6} md={4} key={course.id}>
            <Card>
              <CardContent>
                <Typography variant="h6" gutterBottom>
                  {course.title}
                </Typography>
                <Typography variant="body2" color="text.secondary" gutterBottom>
                  Last accessed: {course.lastAccessed}
                </Typography>
                <Box sx={{ mt: 2 }}>
                  <Typography variant="body2" color="text.secondary">
                    Progress
                  </Typography>
                  <Box
                    sx={{
                      width: '100%',
                      height: 8,
                      bgcolor: 'grey.200',
                      borderRadius: 4,
                      mt: 1,
                    }}
                  >
                    <Box
                      sx={{
                        width: `${course.progress}%`,
                        height: '100%',
                        bgcolor: 'primary.main',
                        borderRadius: 4,
                      }}
                    />
                  </Box>
                  <Typography variant="body2" color="text.secondary" sx={{ mt: 1 }}>
                    {course.progress}% complete
                  </Typography>
                </Box>
              </CardContent>
              <CardActions>
                <Button size="small" color="primary">
                  Continue Learning
                </Button>
              </CardActions>
            </Card>
          </Grid>
        ))}
      </Grid>
    </Container>
  );
};

export default Dashboard; 