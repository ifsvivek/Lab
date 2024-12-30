<?php
// Database connection details
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "student";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Function to implement Selection Sort
function selectionSort(&$arr, $n) {
    for ($i = 0; $i < $n-1; $i++) {
        $minIndex = $i;
        for ($j = $i+1; $j < $n; $j++) {
            if ($arr[$j]['roll_no'] < $arr[$minIndex]['roll_no']) {
                $minIndex = $j;
            }
        }
        // Swap the found minimum element with the first element
        $temp = $arr[$minIndex];
        $arr[$minIndex] = $arr[$i];
        $arr[$i] = $temp;
    }
}

// Fetch student records
$sql = "SELECT distinct * FROM stud";
$result = $conn->query($sql);

// Store records in an array
$students = array();
while($row = $result->fetch_assoc()) {
    $students[] = $row;
}

// Sort the students array using Selection Sort
selectionSort($students, count($students));

// Close the database connection
$conn->close();
?>

<!DOCTYPE html>
<html>
<head>
    <title>Sorted Student Records</title>
    <style>
        table {
            border-collapse: collapse;
            width: 100%;
        }

        th, td {
            text-align: left;
            padding: 8px;
            border: 1px solid #ddd;
        }

        tr:nth-child(even) {
            background-color: #f2f2f2;
        }

        th {
            background-color: #4CAF50;
            color: white;
        }
    </style>
</head>
<body>
    <h2>Sorted Student Records</h2>
    <table>
        <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Roll No.</th>
        </tr>
        <?php foreach ($students as $student): ?>
            <tr>
                <td><?php echo $student['id']; ?></td>
                <td><?php echo $student['name']; ?></td>
                <td><?php echo $student['roll_no']; ?></td>
            </tr>
        <?php endforeach; ?>
    </table>
</body>
</html>