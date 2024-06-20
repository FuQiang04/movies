<php
con= mysqli_connect("Django","admin","password","django");
if(isset($_POST['search'])){
    $searchq = $_POST['search'];
    $searchq = preg_replace("#[^0-9a-z]#i","",$searchq);
    $query = mysqli_query($con,"SELECT * FROM search WHERE name LIKE '%$searchq%'") or die("could not search");
    $count = mysqli_num_rows($query);
    if($count == 0){
        $output = 'There was no search results!';
    }else{
        while($row = mysqli_fetch_array($query)){
            $name = $row['name'];
            $output .= '<div>'.$name.'</div>';
        }
    }
}

?php>