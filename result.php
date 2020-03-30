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
    <?php
    function reArrayFiles(&$file_post) {

        $file_ary = array();
        $file_count = count($file_post['name']);
        $file_keys = array_keys($file_post);
    
        for ($i=0; $i<$file_count; $i++) {
            foreach ($file_keys as $key) {
                $file_ary[$i][$key] = $file_post[$key][$i];
            }
        }
    
        return $file_ary;
    }
    if(isset($_FILES['images'])){
        $file_ary = reArrayFiles($_FILES['images']);

    foreach ($file_ary as $file) {
        $filepath = "images/" . $file['name'];
        if(move_uploaded_file($file['tmp_name'], $filepath)) 
        {
        echo '<img src='.$filepath.' height=150 width=150 id="image" />';
        echo '<input type="text" value="Loading..." id="result" />';
        } 
    }
    }
    // $files = $_FILES['images'];
    // echo $files;

?>
<script> const imager = document.getElementById('image'); </script>
<script src="js/script.js"></script>
</body>
</html>