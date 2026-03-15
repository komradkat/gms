// Dashboard Chart Initialization
function createCharts() {
    const growthCtx = document.getElementById('growthChart');
    if (growthCtx) {
        new Chart(growthCtx, {
            type: 'line',
            data: {
                labels: ['Sep', 'Oct', 'Nov', 'Dec', 'Jan', 'Feb', 'Mar'],
                datasets: [{
                    label: 'Active Members',
                    data: [820, 910, 1050, 1120, 1180, 1230, 1284],
                    borderColor: '#eab308',
                    borderWidth: 5,
                    tension: 0.4,
                    pointRadius: 0,
                    pointHoverRadius: 6
                }]
            },
            options: {
                plugins: { legend: { display: false } },
                scales: {
                    y: { grid: { color: '#27272a' }, ticks: { color: '#a1a1aa' } },
                    x: { grid: { color: '#27272a' }, ticks: { color: '#a1a1aa' } }
                }
            }
        });
    }

    const attendanceCtx = document.getElementById('attendanceChart');
    if (attendanceCtx) {
        new Chart(attendanceCtx, {
            type: 'bar',
            data: {
                labels: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
                datasets: [{
                    label: 'Attendance',
                    data: [184, 201, 173, 245, 267, 312, 189],
                    backgroundColor: '#eab308',
                    borderRadius: 12,
                    barThickness: 28
                }]
            },
            options: {
                plugins: { legend: { display: false } },
                scales: {
                    y: { grid: { color: '#27272a' }, ticks: { color: '#a1a1aa' } },
                    x: { grid: { display: false }, ticks: { color: '#a1a1aa' } }
                }
            }
        });
    }
}

// Initializations
document.addEventListener('DOMContentLoaded', () => {
    createCharts();
    
    // Keyboard shortcut demo
    document.addEventListener('keydown', (e) => {
        if (e.metaKey && e.key === "k") {
            e.preventDefault();
            const searchInput = document.getElementById("searchInput");
            if (searchInput) searchInput.focus();
        }
    });

    console.log('%c✅ GymForge Advanced Dashboard loaded successfully!', 'color:#eab308; font-family:monospace');
});
