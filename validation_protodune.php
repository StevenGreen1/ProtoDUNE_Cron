<html>
<head>
<title>Pandora ProtoDUNE-SP Validation</title>
<h1>Pandora ProtoDUNE-SP Validation</h1>
<link rel="stylesheet" type="text/css" href="mystyle.css">

<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>jQuery UI Datepicker - Default functionality</title>
<link rel="stylesheet" href="//code.jquery.com/ui/1.12.1/themes/base/jquery-ui.css">
<link rel="stylesheet" href="/resources/demos/style.css">
<script src="https://code.jquery.com/jquery-1.12.4.js"></script>
<script src="https://code.jquery.com/ui/1.12.1/jquery-ui.js"></script>
<script>
$( function() 
{
    $( "#datepicker" ).datepicker({
        altField: "#alternate",
        altFormat: "DD, d MM, yy",
        dateFormat: "dd-mm-y",
        minDate: new Date(2018, 6 - 1, 20),
        maxDate: "+0D"
    });
} );
</script>
</head>

<form name="DatePicker" method="post">
    Version:
    <select name="myversion">
        <option value="mcc10_larsoft_v06_81_00_Beam_Cosmics_5GeV_SpaceChargeEffectOn" <?php echo ($_POST['myversion'] == 'mcc10_larsoft_v06_81_00_Beam_Cosmics_5GeV_SpaceChargeEffectOn') ? 'selected' : ''; ?> >mcc10_larsoft_v06_81_00_Beam_Cosmics_5GeV_SpaceChargeEffectOn</option>
        <option value="Beam_Cosmics_5GeV_SpaceChargeEffectOn" <?php echo ($_POST['myversion'] == 'mcc10_larsoft_v06_63_00_Beam_Cosmics_5GeV_SpaceChargeEffectOn') ? 'selected' : ''; ?> >mcc10_larsoft_v06_63_00_Beam_Cosmics_5GeV_SpaceChargeEffectOn</option>
    </select>
    Date:
    <input type="text" id="datepicker" name="datepicker"/> <input type="text" size=30 id="alternate" name="alternate"/>
    <input type="submit">
</form>

<form>
    <input class="MyButton" type="button" value="Diff Table Outputs?" onclick="window.location.href='https://www.hep.phy.cam.ac.uk/~sg568/get_cron_diff.php'" />
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
            $text=nl2br(file_get_contents("$mydir/TableOutput.txt"));
            echo "<p>$text</p>";
        }

        $files = array('COSMIC_RAY',
                       'COSMIC_RAY_MU_MUON_HitsAll.png',
                       'COSMIC_RAY_MU_MUON_HitsEfficiency.png',
                       'COSMIC_RAY_MU_MUON_MomentumAll.png',
                       'COSMIC_RAY_MU_MUON_MomentumEfficiency.png',
                       'COSMIC_RAY_MU_MUON_Completeness.png',
                       'COSMIC_RAY_MU_MUON_Purity.png',
                       'BEAM_PARTICLES',
                       'Electrons and Positrons',
                       'BEAM_PARTICLE_E_ELECTRON_HitsAll.png',
                       'BEAM_PARTICLE_E_ELECTRON_HitsEfficiency.png',
                       'BEAM_PARTICLE_E_ELECTRON_MomentumAll.png',
                       'BEAM_PARTICLE_E_ELECTRON_MomentumEfficiency.png',
                       'BEAM_PARTICLE_E_ELECTRON_Completeness.png',
                       'BEAM_PARTICLE_E_ELECTRON_Purity.png',
                       'Pi Plus',
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

