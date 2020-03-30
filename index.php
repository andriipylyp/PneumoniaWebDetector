<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <?php include 'inc/header.php'; ?>
</head>
<body>
    <?php include 'inc/top.php'; ?>
    <div class="main">
        <div class="title">
            <h1>Pneumonia Web Detector</h1><br>
            <h2>Welcome, please upload foto of lungs below</h2><br>
            <div class="file">
                <form action="result.php" method="post" enctype="multipart/form-data">
                    <input type="file" name="images[]" multiple="multiple"/>
                    <input type="submit" value="Send files" />
                </form>
            </div>
        </div>
    </div>
    
</body>
</html>