// StudentDashboard.js

document.addEventListener('DOMContentLoaded', () => {
    const ctx = document.getElementById('myPieChart').getContext('2d');
    const myPieChart = new Chart(ctx, {
        type: 'pie',
        data: {
            labels: ['Red', 'Blue', 'Yellow'],
            datasets: [{
                data: [10, 20, 30],
                backgroundColor: ['#FF6384', '#36A2EB', '#FFCE56'],
            }],
        },
    });

    window.handleSectionChange = function(section) {
        const mainContent = document.getElementById('main-content');
        let content = '';
        switch (section) {
            case 'mock':
                content = `
                    <h2>Mock Exams</h2>
                    <table>
                        <tr><th>Exam</th><th>Date</th><th>Score</th></tr>
                        <tr><td>JavaScript Basics</td><td>July 15, 2024</td><td>85%</td></tr>
                        <tr><td>React Components</td><td>July 20, 2024</td><td>78%</td></tr>
                        <tr><td>Python Django Fundamentals</td><td>July 25, 2024</td><td>90%</td></tr>
                    </table>`;
                break;
            
            case 'assignments':
                content = `
                    <h2>Assignments</h2>
                    <ul>
                        <li>HTML and CSS Project: Completed</li>
                        <li>React CRUD Application: In Progress</li>
                        <li>Django REST API: Pending</li>
                    </ul>`;
                break;
                
            case 'attendance':
                content = `
                    <h2>Attendance</h2>
                    <p>Total Classes Attended: 120</p>
                    <p>Total Absences: 5</p>`;
                break;
                    
            case 'grades':
                content = `
                    <h2>Grades</h2>
                    <table>
                    <tr><th>Course</th><th>Grade</th></tr>
                    <tr><td>JavaScript</td><td>A</td></tr>
                    <tr><td>React</td><td>B</td></tr>
                    <tr><td>Django</td><td>A</td></tr>
                    <tr><td>MySQL</td><td>B+</td></tr>
                    </table>`;
                break;
                        
            case 'notifications':
                content = `
                    <h2>Notifications</h2>
                        <ul>
                        <li>Upcoming JavaScript Workshop</li>
                        <li>Reminder: React Project Submission Due Tomorrow</li>
                        <li>Python Django Lab Session Rescheduled</li>
                        </ul>`;
                break;
            case 'calendar':
                content = `
                    <h2>Calendar</h2>
                    <p>No upcoming events</p>`;
                break;
                                
            case 'achievements':
                content = `
                    <h2>Achievements</h2>
                    <ul>
                        <li>Completed JavaScript Basics with Distinction</li>
                        <li>Top Performer in React Project Showcase</li>
                        <li>Received Best Project Award in Django Workshop</li>
                    </ul>`;
                break;
                                    
            case 'progress-tracker':
                content = `
                    <h2>Progress Tracker</h2>
                    <p>Track your progress here</p>`;
                break;
            case 'tasks':
                content = `
                    <h2>Tasks</h2>
                    <ul>
                        <li>Complete React Routing Assignment</li>
                        <li>Prepare for MySQL Exam</li>
                        <li>Review Django Models and Views</li>
                    </ul>`;
                break;
            case 'feedback':
                content = `
                    <h2>Feedback</h2>
                    <p>Provide your feedback here</p>`;
                break;
            case 'resources':
                content = `
                        <h2>Resources</h2>
                            <ul>
                            <li>JavaScript and React Tutorials</li>
                            <li>Django Documentation</li>
                            <li>MySQL Cheat Sheet</li>
                        </ul>`;
                break;
                                                    
           case 'events':
                content = `
                    <h2>Events</h2>
                    <ul>
                        <li>Web Development Seminar</li>
                        <li>React Project Showcase</li>
                        <li>Django Workshop</li>
                    </ul>`;
                break;

        }
        mainContent.innerHTML = content;
    }

    window.viewPerformance = function() {
        const performanceModal = document.getElementById('performanceModal');
        performanceModal.style.display = 'flex';

        const ctx = document.getElementById('performanceBarGraph').getContext('2d');
        const performanceBarGraph = new Chart(ctx, {
            type: 'bar',
            data: {
                labels: ['Mock Percentage', 'Exam Marks', 'Attendance Present', 'Attendance Absent'],
                datasets: [{
                    label: 'Performance',
                    data: [85, 75, 90, 10],
                    backgroundColor: ['#4caf50', '#2196f3', '#ff9800', '#f44336'],
                }],
            },
            options: {
                scales: {
                    y: {
                        beginAtZero: true,
                    },
                },
            },
        });
    }

    window.closePerformanceModal = function() {
        const performanceModal = document.getElementById('performanceModal');
        performanceModal.style.display = 'none';
    }
});
