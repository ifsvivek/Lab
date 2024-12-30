
<!DOCTYPE html>
<head>
    <title>Visitor Counter</title>
    <style>
        body {
font-family: Arial, sans-serif;
line-height: 1.6;
margin: 0;
padding: 20px;
background-color: #f4f4f9;
align-items: center;
}
.container {
max-width: 600px;
text-align: center;
margin: auto;
background: pink;
padding: 20px;
border-radius: 5px;

}
h1 {
color: #333;
text-align: center;
}
.counter {
font-size: 24px;
text-align: center;
margin-top: 20px;
}

    </style>
</head>
<body>
    <div class="container">
        <h1>Welcome <br>to<br> Cambridge Institute of Technology!</h1>
<?php
$count = 'counter.txt';

if (!file_exists($count)) 
{
    file_put_contents($count, 0); 
}

$visitorCount = (int)file_get_contents($count);

$visitorCount++;

file_put_contents($count, $visitorCount);
?>
        <p>You are visitor number: <strong><?php echo $visitorCount; ?></strong></p>
    </div>
</body>
</html>
