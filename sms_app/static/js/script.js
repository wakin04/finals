document.addEventListener('DOMContentLoaded', function() {
    // Initialize any interactive elements
    const deleteButtons = document.querySelectorAll('.btn.danger');
    
    deleteButtons.forEach(button => {
        button.addEventListener('click', function(e) {
            if (!confirm('Are you sure you want to delete this item?')) {
                e.preventDefault();
            }
        });
    });
    
    // Initialize grade chart if on grade list page
    if (document.getElementById('gradeChart')) {
        initializeGradeChart();
    }
});

function initializeGradeChart() {
    const chartElement = document.getElementById('gradeChart');
    const grades = [];
    
    // Get grade data from the table
    document.querySelectorAll('table tbody tr').forEach(row => {
        const cells = row.cells;
        grades.push({
            type: cells[0].textContent.trim(),
            score: parseFloat(cells[1].textContent.split('/')[0]),
            max: parseFloat(cells[1].textContent.split('/')[1]),
            percentage: parseFloat(cells[2].textContent)
        });
    });
    
    if (grades.length === 0) {
        chartElement.innerHTML = '<p>No grades to display</p>';
        return;
    }
    
    // Create a simple bar chart with divs
    let chartHTML = '<div class="chart-container">';
    
    grades.forEach(grade => {
        const barWidth = grade.percentage > 100 ? 100 : grade.percentage;
        chartHTML += `
            <div class="chart-row">
                <div class="chart-label">${grade.type}</div>
                <div class="chart-bar-container">
                    <div class="chart-bar" style="width: ${barWidth}%;"></div>
                    <div class="chart-value">${grade.percentage.toFixed(1)}%</div>
                </div>
            </div>
        `;
    });
    
    chartHTML += '</div>';
    chartElement.innerHTML = chartHTML;
    
    // Add dynamic styles for the chart
    const style = document.createElement('style');
    style.textContent = `
        .chart-container {
            width: 100%;
        }
        .chart-row {
            display: flex;
            align-items: center;
            margin-bottom: 0.5rem;
        }
        .chart-label {
            width: 80px;
            font-weight: bold;
        }
        .chart-bar-container {
            flex-grow: 1;
            display: flex;
            align-items: center;
            height: 30px;
            background-color: #ecf0f1;
            position: relative;
        }
        .chart-bar {
            height: 100%;
            background-color: #3498db;
            transition: width 0.5s ease;
        }
        .chart-value {
            position: absolute;
            left: 10px;
            color: white;
            text-shadow: 1px 1px 1px rgba(0,0,0,0.5);
        }
    `;
    document.head.appendChild(style);
}