<html>
<head>
<title>Pandora ProtoDUNE-SP Validation</title>
<h1>Pandora ProtoDUNE-SP Validation</h1>

<head>
    <meta charset="utf-8">
    <title>jQuery UI Datepicker</title>
    <link rel="stylesheet" href="//code.jquery.com/ui/1.11.4/themes/smoothness/jquery-ui.css">
    <script src="//code.jquery.com/jquery-1.10.2.js"></script>
    <script src="//code.jquery.com/ui/1.11.4/jquery-ui.js"></script>
    <link rel="stylesheet" href="/resources/demos/style.css">
    <script>
        $(function() {
        $( "#datepicker" ).datepicker({
          altField: "#alternate",
          altFormat: "DD, d MM, yy",
          dateFormat: "dd-mm-y",
          minDate: new Date(2018, 6 - 1, 20),
          maxDate: "+0D"
        });
        });
    </script>
</head>

<form name="DatePicker" method="post">
    Version:
    <select name="myversion">
        <option value="Beam_Cosmics_5GeV_SpaceChargeEffectOn" <?php echo ($_POST['myversion'] == 'mcc10_Beam_Cosmics_5GeV_SpaceChargeEffectOn') ? 'selected' : ''; ?> >Beam_Cosmics_5GeV_SpaceChargeEffectOn</option>
    </select>
    Date:
    <input type="text" id="datepicker" name="datepicker"/> <input type="text" size=30 id="alternate" name="alternate"/>
    <input type="submit">
</form>

<body>
    <?php
        $myversion=$_POST['myversion'];
        $mydate=$_POST['datepicker'];
        $myaltDate=$_POST['alternate'];

        echo "<h4>$myversion</h4>";
        echo "<h4>$myaltDate</h4>";

        $yy = substr($mydate,6,2);
        $mm = substr($mydate,3,2);
        $dd = substr($mydate,0,2);

        $newDateFormat = "20".$yy."_".$mm."_".$dd;

        if (!empty($mydate))
        {
            echo "<h4>$newDateFormat</h4>";
        }

        $mydir="CronResults/".$newDateFormat."/".$myversion."/RootFiles";

        if (file_exists($mydir. '/CorrectEventList.txt'))
        {
            echo "List of <a href=$mydir/CorrectEventList.txt>correct events</a><br/><br/>";
        }

        if (file_exists($mydir. '/TableOutput.txt'))
        {
            echo "<p><iframe src='$mydir/TableOutput.txt' frameborder='0' height='400' width='95%'></iframe></p>";
        }

        $files = array('COSMIC_RAY',
                       'COSMIC_RAY_MU_MUON_HitsAll.png',
                       'COSMIC_RAY_MU_MUON_HitsEfficiency.png',
                       'COSMIC_RAY_MU_MUON_MomentumAll.png',
                       'COSMIC_RAY_MU_MUON_MomentumEfficiency.png',
                       'COSMIC_RAY_MU_MUON_Completeness.png',
                       'COSMIC_RAY_MU_MUON_Purity.png',
                       'BEAM_PARTICLES',
                       'BEAM_PARTICLE_E_ELECTRON_HitsAll.png',
                       'BEAM_PARTICLE_E_ELECTRON_HitsEfficiency.png',
                       'BEAM_PARTICLE_E_ELECTRON_MomentumAll.png',
                       'BEAM_PARTICLE_E_ELECTRON_MomentumEfficiency.png',
                       'BEAM_PARTICLE_E_ELECTRON_Completeness.png',
                       'BEAM_PARTICLE_E_ELECTRON_Purity.png',
                       'BEAM_PARTICLE_PI_PLUS_PIPLUS_HitsAll.png',
                       'BEAM_PARTICLE_PI_PLUS_PIPLUS_HitsEfficiency.png',
                       'BEAM_PARTICLE_PI_PLUS_PIPLUS_MomentumAll.png',
                       'BEAM_PARTICLE_PI_PLUS_PIPLUS_MomentumEfficiency.png',
                       'BEAM_PARTICLE_PI_PLUS_PIPLUS_Completeness.png',
                       'BEAM_PARTICLE_PI_PLUS_PIPLUS_Purity.png'
                       );

        for ($i = 0; $i < count($files); $i++)
        {
            $image = $mydir.'/'.$files[$i];

            if (!(empty($mydate)) && (strpos($files[$i], 'png') == false))
            {
                echo "<h4>$files[$i]</h4>";
            }

            if (file_exists($image))
            {
                echo "<img src=$image title=$files[$i] width='25%'/>";
            }
        }
    ?> 
</body>
</html>

