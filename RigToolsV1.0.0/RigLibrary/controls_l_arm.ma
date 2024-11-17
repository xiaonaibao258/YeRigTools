//Maya ASCII 2022 scene
//Name: controls_l_arm.ma
//Last modified: Sat, Sep 14, 2024 02:21:11 PM
//Codeset: 936
requires maya "2022";
requires -nodeType "displayPoints" "Type" "2.0a";
requires -nodeType "connectionOverride" "renderSetup.py" "1.0";
requires "stereoCamera" "10.0";
requires "mtoa" "4.0.2";
currentUnit -l centimeter -a degree -t ntsc;
fileInfo "application" "maya";
fileInfo "product" "Maya 2022";
fileInfo "version" "2022";
fileInfo "cutIdentifier" "202102181415-29bfc1879c";
fileInfo "osv" "Windows 10 Pro v2009 (Build: 19045)";
fileInfo "UUID" "EEA9A8A6-4F23-EC1D-E05D-6A9A25504CC3";
createNode transform -s -n "persp";
	rename -uid "A8135533-4E31-0BCA-499A-EE8BDB1A2627";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 103.95398266966149 182.07035982093549 77.431657427596804 ;
	setAttr ".r" -type "double3" -36.338352750210021 -4280.5999999991118 0 ;
createNode camera -s -n "perspShape" -p "persp";
	rename -uid "C79DD49C-45E2-2170-9DFE-E982098DF4A3";
	setAttr -k off ".v" no;
	setAttr ".fl" 34.999999999999993;
	setAttr ".fcp" 100000;
	setAttr ".coi" 126.91020186368587;
	setAttr ".imn" -type "string" "persp";
	setAttr ".den" -type "string" "persp_depth";
	setAttr ".man" -type "string" "persp_mask";
	setAttr ".tp" -type "double3" 49.213280940216762 101.61139398241005 17.439695910777807 ;
	setAttr ".hc" -type "string" "viewSet -p %camera";
createNode transform -s -n "top";
	rename -uid "5150D538-4F9C-B5A2-11D4-5FA6DE66F410";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 0 1000.1 0 ;
	setAttr ".r" -type "double3" -90 0 0 ;
createNode camera -s -n "topShape" -p "top";
	rename -uid "2B0C9BC9-459F-0660-68BB-529FAC228BB7";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".fcp" 100000;
	setAttr ".coi" 1000.1;
	setAttr ".ow" 30;
	setAttr ".imn" -type "string" "top";
	setAttr ".den" -type "string" "top_depth";
	setAttr ".man" -type "string" "top_mask";
	setAttr ".hc" -type "string" "viewSet -t %camera";
	setAttr ".o" yes;
createNode transform -s -n "front";
	rename -uid "CBCBBE32-4E26-7853-2685-738EA7A66672";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 42.863245291465141 0.36882470639056208 1000.2581164557257 ;
createNode camera -s -n "frontShape" -p "front";
	rename -uid "9CB93752-40A2-C67A-3B5B-64B0DCD792E5";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".fcp" 100000;
	setAttr ".coi" 1001.1122555176338;
	setAttr ".ow" 48.123879526444867;
	setAttr ".imn" -type "string" "front";
	setAttr ".den" -type "string" "front_depth";
	setAttr ".man" -type "string" "front_mask";
	setAttr ".tp" -type "double3" 42.863245291465141 0.36882470639056208 -0.85413906190803779 ;
	setAttr ".hc" -type "string" "viewSet -f %camera";
	setAttr ".o" yes;
createNode transform -s -n "side";
	rename -uid "25B9A76D-4D03-6193-5A2F-B394824EA46C";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 1000.1 0 0 ;
	setAttr ".r" -type "double3" 0 90 0 ;
createNode camera -s -n "sideShape" -p "side";
	rename -uid "2B4A334D-4451-A9BE-BD5B-908ED096E291";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".fcp" 100000;
	setAttr ".coi" 1000.1;
	setAttr ".ow" 47.886214797652592;
	setAttr ".imn" -type "string" "side";
	setAttr ".den" -type "string" "side_depth";
	setAttr ".man" -type "string" "side_mask";
	setAttr ".hc" -type "string" "viewSet -s %camera";
	setAttr ".o" yes;
createNode transform -n "transform1";
	rename -uid "4407EA89-403E-AF2C-C34D-54A5719E495F";
	setAttr ".hio" yes;
createNode displayPoints -n "displayPoints1" -p "transform1";
	rename -uid "E47405D4-48FD-1D17-36F0-62AA18094315";
	setAttr -k off ".v";
	setAttr ".hio" yes;
createNode transform -n "control_transform1";
	rename -uid "C9710D5B-4114-10C9-3590-E9800CDE730C";
	setAttr ".hio" yes;
createNode displayPoints -n "displayPoints1" -p "control_transform1";
	rename -uid "3BDA9096-4149-005D-EBA7-408680059635";
	setAttr -k off ".v";
	setAttr ".hio" yes;
createNode transform -n "grp_l_arm";
	rename -uid "84CD1E13-4450-782D-986A-119E291ACC91";
createNode transform -n "grp_l_armIk" -p "grp_l_arm";
	rename -uid "8CCD1525-4517-3E23-A045-35B3DE0F3DB7";
createNode transform -n "zero_l_handIk" -p "grp_l_armIk";
	rename -uid "006D6914-4AE2-D336-C7A4-D395C3B6C6D4";
	setAttr ".t" -type "double3" 44.937272963155607 104.66738975645308 15.512872252649933 ;
	setAttr ".s" -type "double3" 0.99999999999999967 1.0000000000000004 1.0000000000000007 ;
createNode transform -n "driven_l_handIk" -p "zero_l_handIk";
	rename -uid "2F5D8BF7-4C5B-999E-8C14-7FBF3DB7E730";
	setAttr ".t" -type "double3" 0 4.2632564145606011e-14 -7.1054273576010019e-15 ;
createNode joint -n "ctrl_l_handIk" -p "driven_l_handIk";
	rename -uid "D3152A8A-430C-455F-6857-3686E6594EE6";
	addAttr -is true -ci true -h true -k true -sn "filmboxTypeID" -ln "filmboxTypeID" 
		-smn 5 -smx 5 -at "short";
	addAttr -is true -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "space" -ln "space" -nn "�ռ��л�" -min 0 -max 5 -en "��:�β�:�ز�:ͷ��" 
		-at "enum";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 31;
	setAttr ".t" -type "double3" 0 -1.4210854715202004e-14 -1.7763568394002505e-15 ;
	setAttr -cb on ".ro" 3;
	setAttr ".s" -type "double3" 1.0000000000000002 1 1.0000000000000002 ;
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".jo" -type "double3" 0 -36.630270258457962 -52.885982058048135 ;
	setAttr ".bps" -type "matrix" 0.52069358265761112 -0.52257530910163019 0.67512461019912284 0
		 0.70838116699342246 0.70583009446253353 -2.1913286975848159e-07 0 -0.47652315287740088 0.47824567333991314 0.73770370793661788 0
		 19.776362192053433 43.630487423077135 5.788008016833027 1;
	setAttr ".ds" 2;
	setAttr -l on -cb off ".radi" 0.495;
	setAttr -l on ".liw";
	setAttr -k on ".space";
createNode nurbsCurve -n "ctrl_l_handIkShape" -p "ctrl_l_handIk";
	rename -uid "B232CE6D-464F-8BB5-633B-DD9A64F6597F";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 6;
	setAttr ".cc" -type "nurbsCurve" 
		1 16 0 no 3
		17 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
		17
		1.2062507737400734 1.5449829100240717 3.9368689039407663
		1.2062507737400476 1.5449833867474889 -4.2239979363056657
		8.5450304359635254 1.5449834268325764 -4.2239979363056417
		8.5450304359635076 1.5449829501092214 3.9368689039407667
		1.2062507737400734 1.5449829100240717 3.9368689039407663
		1.2062507938726446 -2.9700152838502509 3.9368685585790972
		1.2062507938726375 -2.9700148071267893 -4.2239982816673054
		1.2062507737400476 1.5449833867474889 -4.2239979363056657
		1.2062507737400734 1.5449829100240717 3.9368689039407663
		1.2062507938726446 -2.9700152838502509 3.9368685585790972
		8.5450304560960753 -2.9700152437650509 3.9368685585791066
		8.5450304359635076 1.5449829501092214 3.9368689039407667
		8.5450304359635254 1.5449834268325764 -4.2239979363056417
		8.5450304560960895 -2.9700147670416559 -4.223998281667301
		8.5450304560960753 -2.9700152437650509 3.9368685585791066
		8.5450304560960895 -2.9700147670416559 -4.223998281667301
		1.2062507938726375 -2.9700148071267893 -4.2239982816673054
		;
createNode transform -n "crv_l_armPvCurve" -p "grp_l_armIk";
	rename -uid "8C980533-41CA-5677-7982-82916E04541C";
	setAttr ".it" no;
createNode nurbsCurve -n "crv_l_armPvCurveShape" -p "crv_l_armPvCurve";
	rename -uid "E678AD53-4481-07D2-D340-E7BACFBE009A";
	setAttr -k off ".v";
	setAttr ".ovdt" 2;
	setAttr ".ove" yes;
	setAttr ".ovc" 1;
	setAttr -s 2 ".cp";
	setAttr ".cc" -type "nurbsCurve" 
		1 1 0 no 3
		2 0 1
		2
		32.347230003372545 121.30594776920708 2.7755575615629387e-16
		40.227936432568882 110.89108329872667 -28.527073322011788
		;
createNode joint -n "jnt_l_upperarmIk" -p "grp_l_armIk";
	rename -uid "B0224C30-45A7-7838-6017-BC9F66F2908F";
	addAttr -is true -ci true -h true -k true -sn "filmboxTypeID" -ln "filmboxTypeID" 
		-smn 5 -smx 5 -at "short";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
	setAttr ".t" -type "double3" 16.05534614221305 142.83672853197766 0 ;
	setAttr ".s" -type "double3" 1.0000000000000011 0.99999999999999989 0.99999999999999944 ;
	setAttr ".jo" -type "double3" 0 0 -52.885982058048178 ;
	setAttr ".bps" -type "matrix" 0.70560300330816084 -0.70815346688471048 0.025358806392828864 0
		 0.70838127767206094 0.70582998338382952 -2.8582741280758217e-07 0 -0.017898803485210876 0.017963905353471431 0.99967841376027 0
		 6.5736090108324836 56.880958696589055 -1.2505882478252854 1;
	setAttr ".radi" 3;
	setAttr -k on ".filmboxTypeID" 5;
createNode joint -n "jnt_l_forearmIk" -p "jnt_l_upperarmIk";
	rename -uid "6765B527-4044-3035-2778-33B9C5C72CF1";
	addAttr -is true -ci true -h true -k true -sn "filmboxTypeID" -ln "filmboxTypeID" 
		-smn 5 -smx 5 -at "short";
	addAttr -is true -ci true -k true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 
		1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
	setAttr ".t" -type "double3" 26.999999999999986 0 2.7755575615629402e-16 ;
	setAttr ".s" -type "double3" 1 0.99999999999999967 1.0000000000000011 ;
	setAttr ".jo" -type "double3" 0 -36.63027025845799 0 ;
	setAttr ".bps" -type "matrix" 0.52069358265761112 -0.52257530910163019 0.67512461019912284 0
		 0.70838121160873679 0.70583004968593899 -2.8820167561338604e-07 0 -0.4765230865539673 0.47824573942449378 0.73770370793659412 0
		 14.569435842471423 48.856231002851104 -0.9632245046490997 1;
	setAttr ".radi" 3;
	setAttr -k on ".filmboxTypeID" 5;
createNode joint -n "jnt_l_handIk" -p "jnt_l_forearmIk";
	rename -uid "203208D7-4C4A-02F4-CA79-4F94F6E898C0";
	addAttr -is true -ci true -h true -k true -sn "filmboxTypeID" -ln "filmboxTypeID" 
		-smn 5 -smx 5 -at "short";
	addAttr -is true -ci true -k true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 
		1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
	setAttr ".t" -type "double3" 25.999999999999993 -2.8421709430404007e-14 -2.8421709430404007e-14 ;
	setAttr ".s" -type "double3" 0.99999999999999967 1.0000000000000002 1 ;
	setAttr ".bps" -type "matrix" 0.52069358265761112 -0.52257530910163019 0.67512461019912284 0
		 0.70838116699342246 0.70583009446253353 -2.1913286975848159e-07 0 -0.47652315287740088 0.47824567333991314 0.73770370793661788 0
		 19.776362192053433 43.630487423077135 5.788008016833027 1;
	setAttr ".radi" 3;
	setAttr -k on ".filmboxTypeID" 5;
createNode transform -n "zero_l_armPv" -p "grp_l_armIk";
	rename -uid "7F2B9809-43AC-8B60-E651-96A19419BA1C";
	setAttr ".ove" yes;
	setAttr ".ovc" 6;
	setAttr ".t" -type "double3" 40.227936432568882 110.89108329872667 -28.527073322011788 ;
	setAttr ".s" -type "double3" 1.0000000000000011 0.99999999999999956 1.0000000000000004 ;
createNode transform -n "driven_l_armPv" -p "zero_l_armPv";
	rename -uid "972FA402-46C3-E62F-0863-FE913B5CAA69";
createNode transform -n "ctrl_l_armPv" -p "driven_l_armPv";
	rename -uid "9F2E1C66-4CF9-104B-687F-03B43897D24F";
	addAttr -ci true -sn "space" -ln "space" -nn "�ռ��л�" -min 0 -max 2 -en "��:����" 
		-at "enum";
	setAttr -k off ".v";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr -k on ".space";
createNode nurbsCurve -n "ctrl_l_armPvShape" -p "ctrl_l_armPv";
	rename -uid "18319972-4331-52C4-EED0-79966169F425";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 12 0 no 3
		13 0 1 2 3 4 5 6 7 8 9 10 11 12
		13
		-3.4889005663334962e-15 1.9344300234227598 1.5994414743559301e-15
		1.934430023422772 -1.2795531794847441e-14 1.5994414743559301e-15
		-3.4889005663334962e-15 -1.2795531794847441e-14 1.9344300234227743
		-3.4889005663334962e-15 1.9344300234227598 1.5994414743559301e-15
		-1.934430023422772 -1.2795531794847441e-14 1.5994414743559301e-15
		-3.4889005663334962e-15 -1.2795531794847441e-14 -1.9344300234227709
		1.934430023422772 -1.2795531794847441e-14 1.5994414743559301e-15
		-3.4889005663334962e-15 -1.9344300234227869 1.5994414743559301e-15
		-3.4889005663334962e-15 -1.2795531794847441e-14 1.9344300234227743
		-1.934430023422772 -1.2795531794847441e-14 1.5994414743559301e-15
		-3.4889005663334962e-15 -1.9344300234227869 1.5994414743559301e-15
		-3.4889005663334962e-15 -1.2795531794847441e-14 -1.9344300234227709
		-3.4889005663334962e-15 1.9344300234227598 1.5994414743559301e-15
		;
createNode transform -n "zero_l_upperarmFk" -p "grp_l_arm";
	rename -uid "45FEAF1A-4857-D1E5-66EC-B69CA4F6906E";
	setAttr ".t" -type "double3" 16.05534614221305 142.83672853197766 0 ;
	setAttr ".r" -type "double3" 0 0 -52.885982058048178 ;
	setAttr ".s" -type "double3" 1.0000000000000011 0.99999999999999989 0.99999999999999944 ;
createNode transform -n "driven_l_upperarmFk" -p "zero_l_upperarmFk";
	rename -uid "AFC24B8B-47F2-EC66-AA81-C8B19719F445";
	setAttr ".t" -type "double3" -1.4210854715202004e-14 -4.2632564145606011e-14 2.8421709430404007e-14 ;
	setAttr ".r" -type "double3" -2.3854160110976384e-15 6.3611093629270351e-15 -1.3241718894150485e-31 ;
	setAttr ".s" -type "double3" 0.99999999999999989 0.99999999999999989 0.99999999999999978 ;
createNode transform -n "ctrl_l_upperarmFk" -p "driven_l_upperarmFk";
	rename -uid "C1CCCEB7-4160-8E48-07CA-1994B03FC6E8";
	addAttr -ci true -sn "subCtrlVis" -ln "subCtrlVis" -nn "�μ���������ʾ" -min 0 
		-max 1 -at "bool";
	addAttr -ci true -sn "rotateFollow" -ln "rotateFollow" -nn "��ת����" -min 0 -max 
		1 -at "double";
	setAttr -l on -k off ".v";
	setAttr -cb on ".ro";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr -cb on ".subCtrlVis" yes;
	setAttr -k on ".rotateFollow";
createNode nurbsCurve -n "ctrl_l_upperarmFkShape" -p "ctrl_l_upperarmFk";
	rename -uid "063E50AD-4601-560A-F25C-69AFF747C3D3";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 6;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		6.9148596327625027 6.6635154612108867 -8.6622346165258666
		6.9148596327624654 -0.51953102520430661 -12.768055501014405
		6.9148596327625027 -7.7025775116195021 -8.6622346165258666
		6.9148596327625027 -10.677892785449048 -1.4791881301107059
		6.9148596327625027 -7.7025775116195021 5.7038583563045107
		6.9148596327625027 -0.51953102520429006 9.5993040266234431
		6.9148596327625027 6.6635154612108867 5.7038583563045107
		6.9148596327625027 9.6388307350405 -1.4791881301107046
		6.9148596327625027 6.6635154612108867 -8.6622346165258666
		6.9148596327624654 -0.51953102520430661 -12.768055501014405
		6.9148596327625027 -7.7025775116195021 -8.6622346165258666
		;
createNode transform -n "output_l_upperarmFk" -p "ctrl_l_upperarmFk";
	rename -uid "7C1C16E1-44B6-25CC-9F32-0FBEB9B51127";
createNode transform -n "zero_l_forearmFk" -p "output_l_upperarmFk";
	rename -uid "F279F452-4932-2608-7C00-49B4AF739F9C";
	setAttr ".t" -type "double3" 27 1.4210854715202004e-14 -2.7644553313166407e-14 ;
	setAttr ".r" -type "double3" 0 -36.63027025845799 0 ;
	setAttr ".s" -type "double3" 1 0.99999999999999978 1.0000000000000013 ;
createNode transform -n "ctrl_l_forearmFk" -p "zero_l_forearmFk";
	rename -uid "B71DC502-4AD1-96C7-743B-CB8FE04E5598";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "zero_l_handFk" -p "ctrl_l_forearmFk";
	rename -uid "1E11F61A-4579-ABE5-1DF7-1493C8BC4B18";
	setAttr ".t" -type "double3" 25.999999999999986 -2.8421709430404007e-14 0 ;
	setAttr ".s" -type "double3" 0.99999999999999956 0.99999999999999978 1.0000000000000007 ;
createNode transform -n "driven_l_handFk" -p "zero_l_handFk";
	rename -uid "FDE27F0C-4099-3D2C-1CEE-3A90D5234CB9";
createNode transform -n "ctrl_l_handFk" -p "driven_l_handFk";
	rename -uid "DE5EDAE7-411F-4AF7-2572-37ABD0C2CE19";
	addAttr -ci true -sn "rotateFollow" -ln "rotateFollow" -nn "��ת����" -min 0 -max 
		1 -at "double";
	setAttr -l on -k off ".v";
	setAttr -cb on ".ro" 3;
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" -8.8817841970012523e-15 1.4210854715202007e-14 -3.5527136788005017e-15 ;
	setAttr ".sp" -type "double3" -8.8817841970012523e-15 1.4210854715202004e-14 -3.5527136788005009e-15 ;
	setAttr ".spt" -type "double3" 0 3.1554436208840479e-30 -7.8886090522101198e-31 ;
	setAttr -k on ".rotateFollow";
createNode nurbsCurve -n "ctrl_l_handFkShape" -p "ctrl_l_handFk";
	rename -uid "0833F42D-4B93-60CF-F243-8092BEF556E4";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 6;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		-1.9800300073537167e-14 4.7548216454271897 -5.1486818874121782
		-1.986721850351294e-14 -0.4181245493976376 -7.2913863587349148
		-1.9800300073537167e-14 -5.5910707442225371 -5.1486818874121782
		-1.9638744692316578e-14 -7.7337752155452879 0.024264307412658812
		-1.9477189311096153e-14 -5.5910707442225371 5.1972105022375352
		-1.9410270881120373e-14 -0.41812454939763843 7.3399149735603055
		-1.9477189311096153e-14 4.7548216454271897 5.1972105022375352
		-1.9638744692316578e-14 6.8975261167499342 0.024264307412658975
		-1.9800300073537167e-14 4.7548216454271897 -5.1486818874121782
		-1.986721850351294e-14 -0.4181245493976376 -7.2913863587349148
		-1.9800300073537167e-14 -5.5910707442225371 -5.1486818874121782
		;
createNode nurbsCurve -n "ctrl_l_forearmFkShape" -p "ctrl_l_forearmFk";
	rename -uid "93D998D4-4477-E6A2-AB54-85B3B4014FDF";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 6;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		5.3939909159070547 5.811787693454729 -7.1687188093733996
		5.3939909159070547 -0.62569696021071985 -9.8352122604903247
		5.3939909159070547 -7.0631816138762984 -7.1687188093733996
		5.3939909159070547 -9.7296750649931898 -0.73123415570784378
		5.3939909159070547 -7.0631816138762984 5.7062504979576119
		5.3939909159070547 -0.62569696021072152 8.3727439490745645
		5.3939909159070547 5.811787693454729 5.7062504979576119
		5.3939909159070547 8.4782811445716764 -0.73123415570784212
		5.3939909159070547 5.811787693454729 -7.1687188093733996
		5.3939909159070547 -0.62569696021071985 -9.8352122604903247
		5.3939909159070547 -7.0631816138762984 -7.1687188093733996
		;
createNode transform -n "crv_l_armFkPv" -p "output_l_upperarmFk";
	rename -uid "853D7ED8-4BE8-DA32-42CC-7794DE3352A5";
	setAttr -k off -cb on ".v" no;
	setAttr ".ovdt" 2;
	setAttr ".t" -type "double3" 40.060433980601545 1.4210854715202004e-14 -28.527073322011841 ;
	setAttr ".r" -type "double3" 0 0 52.885982058048207 ;
	setAttr -l on ".sx";
	setAttr -l on ".sy";
	setAttr -l on ".sz";
createNode nurbsCurve -n "crv_l_armFkPvShape" -p "crv_l_armFkPv";
	rename -uid "A75F42D5-414A-2FBD-FF83-82B2BCD5EB89";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 7 0 no 3
		8 0 1 2 3 4 5 6 7
		8
		2.3222806611432958 0 0
		-2.3222806611432958 0 0
		0 0 0
		0 0 2.3222806611432958
		0 0 -2.3222806611432958
		0 0 0
		0 2.3222806611432958 0
		0 -2.3222806611432958 0
		;
createNode transform -n "ctrl_l_upperarmSub" -p "ctrl_l_upperarmFk";
	rename -uid "71E5B619-4C8B-3C3B-0088-E88D31CBF342";
	setAttr -k off ".v";
	setAttr ".t" -type "double3" -1.4210854715202004e-14 2.8421709430404007e-14 -4.9960036108132044e-16 ;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode nurbsCurve -n "ctrl_l_upperarmSubShape" -p "ctrl_l_upperarmSub";
	rename -uid "372A0448-48A0-B425-2798-8F946F7A4B94";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 5;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		6.9185945297745066 6.1108379313697316 -8.1125986441830022
		6.9185945297745022 -0.51802313109764386 -11.901647795142146
		6.9185945297745066 -7.1468841935650236 -8.1125986441830022
		6.9185945297745066 -9.8926483487258814 -1.4837375817156622
		6.9185945297745066 -7.1468841935650236 5.145123480751737
		6.9185945297745066 -0.51802313109762732 8.7400282574046937
		6.9185945297745066 6.1108379313697316 5.145123480751737
		6.9185945297745066 8.8566020865306676 -1.4837375817156586
		6.9185945297745066 6.1108379313697316 -8.1125986441830022
		6.9185945297745022 -0.51802313109764386 -11.901647795142146
		6.9185945297745066 -7.1468841935650236 -8.1125986441830022
		;
createNode transform -n "grp_l_finger" -p "grp_l_arm";
	rename -uid "BA87530A-4F1E-C3BD-0DC3-85966549E07F";
	setAttr ".t" -type "double3" 44.937272963155607 104.66738975645308 15.512872252649933 ;
	setAttr ".r" -type "double3" 1.9816481591986373e-15 -36.63027025845799 -52.885982058048178 ;
	setAttr ".s" -type "double3" 0.99999999999999967 1.0000000000000004 1.0000000000000007 ;
createNode transform -n "zero_l_finThumbA" -p "grp_l_finger";
	rename -uid "3505C725-40F8-C839-2342-E2B88BD980CE";
	setAttr ".t" -type "double3" 2.0096670930267635 -2.3853699944757523 2.0501371176112713 ;
	setAttr ".r" -type "double3" 92.8995702166591 -25.516719342734657 -37.146806414413014 ;
	setAttr ".s" -type "double3" 0.99999999999999989 1.0000000000000002 1.0000000000000004 ;
createNode transform -n "driven_l_finThumbA" -p "zero_l_finThumbA";
	rename -uid "D9900F62-4388-94E7-D6FB-63BA71551EAC";
	setAttr ".t" -type "double3" 6.0396132539608516e-14 0 1.6875389974302379e-14 ;
	setAttr ".r" -type "double3" 1.7393658414253607e-15 4.2738703532166022e-16 -1.319433231138381e-14 ;
createNode transform -n "ctrl_l_finThumbA" -p "driven_l_finThumbA";
	rename -uid "C8F302B5-432A-B366-4094-6888498C4ED6";
	addAttr -ci true -sn "fingerBent" -ln "fingerBent" -nn "��ָ����" -at "double";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 0 0 1.4210854715202004e-14 ;
	setAttr ".sp" -type "double3" 0 0 1.4210854715202004e-14 ;
	setAttr -k on ".fingerBent";
createNode transform -n "zero_l_finThumbB" -p "ctrl_l_finThumbA";
	rename -uid "B0D7341D-4785-E813-35F8-6F86B3ACBF89";
	setAttr ".t" -type "double3" 4.2998591652410028 0 -1.4210854715202004e-14 ;
	setAttr ".r" -type "double3" 0 0 -18.812370273744008 ;
	setAttr ".s" -type "double3" 1.0000000000000007 1 1 ;
createNode transform -n "offset_l_finThumbB" -p "zero_l_finThumbB";
	rename -uid "58A5E313-4B70-A031-6F18-26B1DE401068";
	setAttr ".t" -type "double3" 2.8421709430404007e-14 -1.4210854715202004e-14 8.8817841970012523e-16 ;
	setAttr ".s" -type "double3" 0.99999999999999989 0.99999999999999978 0.99999999999999989 ;
createNode transform -n "ctrl_l_finThumbB" -p "offset_l_finThumbB";
	rename -uid "2031ABA9-4527-A1A4-00E4-81872C85C97B";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 0 -3.5527136788005001e-15 3.5527136788005001e-15 ;
	setAttr ".sp" -type "double3" 0 -3.5527136788005009e-15 3.5527136788005009e-15 ;
	setAttr ".spt" -type "double3" 0 7.8886090522101163e-31 -7.8886090522101163e-31 ;
createNode transform -n "zero_l_finThumbC" -p "ctrl_l_finThumbB";
	rename -uid "FE4E02FF-473D-4EC0-7298-E3BA757FB2A5";
	setAttr ".t" -type "double3" 3.1999999999999886 -7.1054273576010019e-15 -4.2632564145606011e-14 ;
	setAttr ".r" -type "double3" 0 0 -12.055499772937118 ;
	setAttr ".s" -type "double3" 0.99999999999999967 0.999999999999999 0.99999999999999922 ;
createNode transform -n "offset_l_finThumbC" -p "zero_l_finThumbC";
	rename -uid "0C5C950C-4D67-5CBA-A6DA-4CA234C2B5CB";
	setAttr ".t" -type "double3" 2.8421709430404007e-14 -1.4210854715202004e-14 8.8817841970012523e-16 ;
	setAttr ".s" -type "double3" 0.99999999999999989 0.99999999999999978 0.99999999999999989 ;
createNode transform -n "ctrl_l_finThumbC" -p "offset_l_finThumbC";
	rename -uid "ECB7565F-4819-775B-62D0-F4864C638483";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 0 -3.5527136788005001e-15 3.5527136788005001e-15 ;
	setAttr ".sp" -type "double3" 0 -3.5527136788005009e-15 3.5527136788005009e-15 ;
	setAttr ".spt" -type "double3" 0 7.8886090522101163e-31 -7.8886090522101163e-31 ;
createNode nurbsCurve -n "ctrl_l_finThumbCShape" -p "ctrl_l_finThumbC";
	rename -uid "AC4A71EE-4B41-0271-52A6-5CA4ED2949AD";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 6;
	setAttr ".cc" -type "nurbsCurve" 
		3 16 2 no 3
		21 -2 -1 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18
		19
		1.0792648228389274 1.1002819995172426 -0.4991527192480581
		1.0792648228389274 1.1986659181792958 3.5274434928691588e-14
		1.0792648228389274 1.1002819995172426 0.49915271924812049
		1.0792648228389274 0.82010830329492446 0.92231396182135217
		1.0792648228389274 0.40079873498131957 1.2050612645041767
		1.0792648228389274 -0.093810624698533462 1.3043489135738089
		1.0792648228389274 -0.5884199843783875 1.2050612645041767
		1.0792648228389274 -1.0077295526919956 0.92231396182135217
		1.0792648228389274 -1.2879032489143065 0.49915271924812049
		1.0792648228389274 -1.3862871675763628 3.548508238344105e-14
		1.0792648228389274 -1.2879032489143065 -0.49915271924805887
		1.0792648228389274 -1.0077295526919954 -0.92231396182129821
		1.0792648228389274 -0.58841998437838694 -1.2050612645041201
		1.0792648228389274 -0.093810624698533421 -1.3043489135737469
		1.0792648228389274 0.40079873498131979 -1.2050612645041201
		1.0792648228389274 0.8201083032949249 -0.92231396182129799
		1.0792648228389274 1.1002819995172426 -0.4991527192480581
		1.0792648228389274 1.1986659181792958 3.5274434928691588e-14
		1.0792648228389274 1.1002819995172426 0.49915271924812049
		;
createNode nurbsCurve -n "ctrl_l_finThumbBShape" -p "ctrl_l_finThumbB";
	rename -uid "D0B9572E-4658-D16E-D837-409D57B295D2";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 6;
	setAttr ".cc" -type "nurbsCurve" 
		3 16 2 no 3
		21 -2 -1 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18
		19
		1.0792648228389288 1.1572848329491705 -0.48565083324388864
		1.0792648228389288 1.2572488178055441 0.12469568160894587
		1.0792648228389288 1.1572848329491705 0.7350421964617817
		1.0792648228389288 0.87261148889864737 1.2524689872332071
		1.0792648228389288 0.44656772171538611 1.5982025155138075
		1.0792648228389288 -0.05598516714333511 1.7196079857051099
		1.0792648228389288 -0.5585380560020583 1.5982025155138073
		1.0792648228389288 -0.98458182318532117 1.2524689872332071
		1.0792648228389288 -1.2692551672358434 0.73504219646178137
		1.0792648228389288 -1.3692191520922175 0.12469568160894604
		1.0792648228389288 -1.2692551672358434 -0.4856508332438898
		1.0792648228389288 -0.98458182318532061 -1.0030776240153145
		1.0792648228389288 -0.5585380560020583 -1.3488111522959172
		1.0792648228389288 -0.055985167143334826 -1.4702166224872188
		1.0792648228389288 0.44656772171538628 -1.3488111522959172
		1.0792648228389288 0.87261148889864792 -1.0030776240153145
		1.0792648228389288 1.1572848329491705 -0.48565083324388864
		1.0792648228389288 1.2572488178055441 0.12469568160894587
		1.0792648228389288 1.1572848329491705 0.7350421964617817
		;
createNode nurbsCurve -n "ctrl_l_finThumbAShape" -p "ctrl_l_finThumbA";
	rename -uid "CBCD2C25-4FB6-D7A2-5073-B891D0CFD8C3";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 6;
	setAttr ".cc" -type "nurbsCurve" 
		1 17 0 no 3
		18 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17
		18
		9.8595418567213127 0.0030698631815791674 0.0014436059122514776
		9.918443859747951 0.003069863181579164 -0.29467660384204525
		10.100065838564683 0.0030698631815791488 -0.53183187810171406
		10.34473471008085 0.0030698631815791371 -0.69531438215289487
		10.633341322578655 0.0030698631815791184 -0.77235585994508871
		10.929461532332947 0.0030698631815790993 -0.71345385691844843
		11.180500158548202 0.0030698631815790842 -0.54571523005729983
		11.34823878540935 0.0030698631815790716 -0.29467660384204525
		11.407140788435987 0.003069863181579069 0.0014436059122513102
		11.330099310643792 0.0030698631815790742 0.29005021841004108
		11.166616806592616 0.0030698631815790876 0.53471908992621764
		10.929461532332947 0.0030698631815790993 0.716341068742952
		10.633341322578655 0.0030698631815791184 0.75560904079287061
		10.34473471008085 0.0030698631815791371 0.69820159397739745
		10.100065838564683 0.0030698631815791488 0.53471908992621764
		9.9365833345135091 0.0030698631815791631 0.29005021841004108
		9.8791758876980289 0.003069863181579164 0.0014436059122515138
		-0.20201566257708059 1.4210854715202004e-14 -7.1054273576010019e-15
		;
createNode transform -n "zero_l_finIndexA" -p "grp_l_finger";
	rename -uid "6949D473-4B4F-7351-F280-549A93DEF3CD";
	setAttr ".t" -type "double3" 8.6968786195776921 -1.967481627425812 2.1216751291252649 ;
	setAttr ".r" -type "double3" 9.8613845963534743 10.126227935235558 -22.540364524530993 ;
	setAttr ".s" -type "double3" 0.99999999999999989 1 1 ;
createNode transform -n "driven_l_finIndexA" -p "zero_l_finIndexA";
	rename -uid "251034DD-4B14-472C-DE98-DBBCB4792404";
	setAttr ".t" -type "double3" 6.0396132539608516e-14 0 1.6875389974302379e-14 ;
	setAttr ".r" -type "double3" 1.7393658414253607e-15 4.2738703532166022e-16 -1.319433231138381e-14 ;
createNode transform -n "ctrl_l_finIndexA" -p "driven_l_finIndexA";
	rename -uid "6CA9B2E7-4707-0CAC-A389-558562D713B9";
	addAttr -ci true -sn "fingerBent" -ln "fingerBent" -nn "��ָ����" -at "double";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 0 0 1.4210854715202004e-14 ;
	setAttr ".sp" -type "double3" 0 0 1.4210854715202004e-14 ;
	setAttr -av -k on ".fingerBent";
createNode transform -n "zero_l_finIndexB" -p "ctrl_l_finIndexA";
	rename -uid "E61F9B7C-4CE9-86B8-44F5-B1827818E2DD";
	setAttr ".t" -type "double3" 4.5645484924315838 -1.4210854715202004e-14 -1.4210854715202004e-14 ;
	setAttr ".r" -type "double3" 0 0 -9.8848674766800144 ;
	setAttr ".s" -type "double3" 1.0000000000000002 1.0000000000000004 0.99999999999999978 ;
createNode transform -n "offset_l_finIndexB" -p "zero_l_finIndexB";
	rename -uid "EEA0E1C1-4240-BA3F-C9DF-19978F52EBE7";
	setAttr ".t" -type "double3" 2.8421709430404007e-14 -1.4210854715202004e-14 8.8817841970012523e-16 ;
	setAttr ".s" -type "double3" 0.99999999999999989 0.99999999999999978 0.99999999999999989 ;
createNode transform -n "ctrl_l_finIndexB" -p "offset_l_finIndexB";
	rename -uid "A42A5F3F-48D5-2564-1924-68960D89F7CC";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 0 -3.5527136788005001e-15 3.5527136788005001e-15 ;
	setAttr ".sp" -type "double3" 0 -3.5527136788005009e-15 3.5527136788005009e-15 ;
	setAttr ".spt" -type "double3" 0 7.8886090522101163e-31 -7.8886090522101163e-31 ;
createNode transform -n "zero_l_finIndexC" -p "ctrl_l_finIndexB";
	rename -uid "5F7CD03F-44F0-06C3-9019-94BCF4901A5A";
	setAttr ".t" -type "double3" 2.4864709377288676 0 -2.1316282072803006e-14 ;
	setAttr ".r" -type "double3" 0 0 -7.701066592649064 ;
	setAttr ".s" -type "double3" 0.99999999999999978 1.0000000000000007 0.99999999999999978 ;
createNode transform -n "offset_l_finIndexC" -p "zero_l_finIndexC";
	rename -uid "46589FBF-4B0A-E50F-D496-75B209193F13";
	setAttr ".t" -type "double3" 2.8421709430404007e-14 -1.4210854715202004e-14 8.8817841970012523e-16 ;
	setAttr ".s" -type "double3" 0.99999999999999989 0.99999999999999978 0.99999999999999989 ;
createNode transform -n "ctrl_l_finIndexC" -p "offset_l_finIndexC";
	rename -uid "F9195524-4B49-5018-4727-5EB191949521";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 0 -3.5527136788005001e-15 3.5527136788005001e-15 ;
	setAttr ".sp" -type "double3" 0 -3.5527136788005009e-15 3.5527136788005009e-15 ;
	setAttr ".spt" -type "double3" 0 7.8886090522101163e-31 -7.8886090522101163e-31 ;
createNode nurbsCurve -n "ctrl_l_finIndexCShape" -p "ctrl_l_finIndexC";
	rename -uid "A12819C5-40FC-B017-BEF7-40AF613B2B29";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 6;
	setAttr ".cc" -type "nurbsCurve" 
		3 16 2 no 3
		21 -2 -1 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18
		19
		1.0792648228389323 1.3550738816387857 -0.4706993426626771
		1.0792648228389323 1.4667214003057614 0.024042463391749449
		1.0792648228389323 1.3550738816387857 0.51878426944616784
		1.0792648228389323 1.0371286482676261 0.93820612037444395
		1.0792648228389323 0.5612899797923333 1.218454841441291
		1.0792648228389323 -7.6413881372449937e-15 1.3168651053252689
		1.0792648228389323 -0.5612899797923534 1.2184548414412901
		1.0792648228389323 -1.0371286482676489 0.93820612037444395
		1.0792648228389323 -1.3550738816388108 0.51878426944616773
		1.0792648228389323 -1.4667214003057805 0.024042463391749667
		1.0792648228389323 -1.3550738816388099 -0.4706993426626781
		1.0792648228389323 -1.0371286482676481 -0.8901211935909582
		1.0792648228389323 -0.5612899797923534 -1.1703699146578077
		1.0792648228389323 -7.3217564081998967e-15 -1.2687801785417794
		1.0792648228389323 0.56128997979233353 -1.1703699146578059
		1.0792648228389323 1.0371286482676261 -0.8901211935909582
		1.0792648228389323 1.3550738816387857 -0.4706993426626771
		1.0792648228389323 1.4667214003057614 0.024042463391749449
		1.0792648228389323 1.3550738816387857 0.51878426944616784
		;
createNode nurbsCurve -n "ctrl_l_finIndexBShape" -p "ctrl_l_finIndexB";
	rename -uid "E5D9BDEC-4827-0872-F2B5-818815C00DF7";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 6;
	setAttr ".cc" -type "nurbsCurve" 
		3 16 2 no 3
		21 -2 -1 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18
		19
		1.0792648228389263 1.4522641227687514 -0.48875837514304127
		1.0792648228389263 1.5673569686821283 1.8658194723008115e-14
		1.0792648228389263 1.4522641227687514 0.48875837514307746
		1.0792648228389263 1.124507427499692 0.90310771827630953
		1.0792648228389263 0.63398486860781711 1.1799670979938295
		1.0792648228389263 0.055374059086350284 1.2771871834701696
		1.0792648228389263 -0.52323675043510598 1.1799670979938275
		1.0792648228389263 -1.0137593093269741 0.90310771827630953
		1.0792648228389263 -1.3415160045960273 0.48875837514307746
		1.0792648228389263 -1.4566088505093981 1.8864455660274824e-14
		1.0792648228389263 -1.3415160045960268 -0.48875837514304216
		1.0792648228389263 -1.0137593093269737 -0.90310771827627256
		1.0792648228389263 -0.52323675043510598 -1.179967097993794
		1.0792648228389263 0.055374059086350597 -1.2771871834701305
		1.0792648228389263 0.63398486860781755 -1.179967097993794
		1.0792648228389263 1.1245074274996936 -0.90310771827627245
		1.0792648228389263 1.4522641227687514 -0.48875837514304127
		1.0792648228389263 1.5673569686821283 1.8658194723008115e-14
		1.0792648228389263 1.4522641227687514 0.48875837514307746
		;
createNode nurbsCurve -n "ctrl_l_finIndexAShape" -p "ctrl_l_finIndexA";
	rename -uid "D9F1C318-409D-9C30-00B6-B4BC05865A9C";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 6;
	setAttr ".cc" -type "nurbsCurve" 
		1 17 0 no 3
		18 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17
		18
		9.8595418567213127 0.0030698631815791674 0.0014436059122514776
		9.918443859747951 0.003069863181579164 -0.29467660384204525
		10.100065838564683 0.0030698631815791488 -0.53183187810171406
		10.34473471008085 0.0030698631815791371 -0.69531438215289487
		10.633341322578655 0.0030698631815791184 -0.77235585994508871
		10.929461532332947 0.0030698631815790993 -0.71345385691844843
		11.180500158548202 0.0030698631815790842 -0.54571523005729983
		11.34823878540935 0.0030698631815790716 -0.29467660384204525
		11.407140788435987 0.003069863181579069 0.0014436059122513102
		11.330099310643792 0.0030698631815790742 0.29005021841004108
		11.166616806592616 0.0030698631815790876 0.53471908992621764
		10.929461532332947 0.0030698631815790993 0.716341068742952
		10.633341322578655 0.0030698631815791184 0.75560904079287061
		10.34473471008085 0.0030698631815791371 0.69820159397739745
		10.100065838564683 0.0030698631815791488 0.53471908992621764
		9.9365833345135091 0.0030698631815791631 0.29005021841004108
		9.8791758876980289 0.003069863181579164 0.0014436059122515138
		-0.20201566257708059 1.4210854715202004e-14 -7.1054273576010019e-15
		;
createNode transform -n "zero_l_finMidA" -p "grp_l_finger";
	rename -uid "F4F0FD14-42BD-C816-81FD-DDB7C41B6346";
	setAttr ".t" -type "double3" 8.6169257617442696 -0.90969331213706539 -0.10898977399086363 ;
	setAttr ".r" -type "double3" 4.0722263355242008e-16 12.500322402108456 -26.102138828425208 ;
	setAttr ".s" -type "double3" 0.99999999999999989 1 1 ;
createNode transform -n "driven_l_finMidA" -p "zero_l_finMidA";
	rename -uid "E68158A2-44F5-E1C2-4A9E-7E8673000A6B";
	setAttr ".t" -type "double3" 6.0396132539608516e-14 0 1.6875389974302379e-14 ;
	setAttr ".r" -type "double3" 1.7393658414253607e-15 4.2738703532166022e-16 -1.319433231138381e-14 ;
createNode transform -n "ctrl_l_finMidA" -p "driven_l_finMidA";
	rename -uid "C36F0920-446D-FE96-72D1-B4ACBB0EE33A";
	addAttr -ci true -sn "fingerBent" -ln "fingerBent" -nn "��ָ����" -at "double";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 0 0 1.4210854715202004e-14 ;
	setAttr ".sp" -type "double3" 0 0 1.4210854715202004e-14 ;
	setAttr -av -k on ".fingerBent";
createNode transform -n "zero_l_finMidB" -p "ctrl_l_finMidA";
	rename -uid "EDDF63A6-43F5-A852-C2B6-4F8EF36D0A81";
	setAttr ".t" -type "double3" 4.9196705818175843 -4.2632564145606011e-14 -1.4210854715202004e-14 ;
	setAttr ".r" -type "double3" 0 0 -17.432490422875034 ;
	setAttr ".s" -type "double3" 1.0000000000000002 1.0000000000000004 0.99999999999999967 ;
createNode transform -n "offset_l_finMidB" -p "zero_l_finMidB";
	rename -uid "72D1A834-4EF5-31A7-B9FC-A1969A586044";
	setAttr ".t" -type "double3" 2.8421709430404007e-14 -1.4210854715202004e-14 8.8817841970012523e-16 ;
	setAttr ".s" -type "double3" 0.99999999999999989 0.99999999999999978 0.99999999999999989 ;
createNode transform -n "ctrl_l_finMidB" -p "offset_l_finMidB";
	rename -uid "15A0A2B7-441F-49A0-699C-B19A4837D603";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 0 -3.5527136788005001e-15 3.5527136788005001e-15 ;
	setAttr ".sp" -type "double3" 0 -3.5527136788005009e-15 3.5527136788005009e-15 ;
	setAttr ".spt" -type "double3" 0 7.8886090522101163e-31 -7.8886090522101163e-31 ;
createNode transform -n "zero_l_finMidC" -p "ctrl_l_finMidB";
	rename -uid "ACF06E78-4764-8FC0-A00E-7A9B4762A3AC";
	setAttr ".t" -type "double3" 2.899371529353175 1.4210854715202004e-14 7.1054273576010019e-15 ;
	setAttr ".r" -type "double3" 0 0 -15.602983687247056 ;
	setAttr ".s" -type "double3" 0.99999999999999956 1.0000000000000004 0.99999999999999967 ;
createNode transform -n "offset_l_finMidC" -p "zero_l_finMidC";
	rename -uid "A2D4325C-44A4-E185-8014-2AAEB77516B1";
	setAttr ".t" -type "double3" 2.8421709430404007e-14 -1.4210854715202004e-14 8.8817841970012523e-16 ;
	setAttr ".s" -type "double3" 0.99999999999999989 0.99999999999999978 0.99999999999999989 ;
createNode transform -n "ctrl_l_finMidC" -p "offset_l_finMidC";
	rename -uid "9104FBF1-492E-B825-ED83-259151588D1E";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 0 -3.5527136788005001e-15 3.5527136788005001e-15 ;
	setAttr ".sp" -type "double3" 0 -3.5527136788005009e-15 3.5527136788005009e-15 ;
	setAttr ".spt" -type "double3" 0 7.8886090522101163e-31 -7.8886090522101163e-31 ;
createNode nurbsCurve -n "ctrl_l_finMidCShape" -p "ctrl_l_finMidC";
	rename -uid "C2377056-4819-2580-0F6A-03839E7BFD30";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 6;
	setAttr ".cc" -type "nurbsCurve" 
		3 16 2 no 3
		21 -2 -1 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18
		19
		1.0792648228389228 1.0889606993503318 -0.23920153442093847
		1.0792648228389228 1.20840342398621 0.26420540172793322
		1.0792648228389228 1.0889606993503318 0.76761233787681094
		1.0792648228389228 0.74881659751751273 1.1943801313922568
		1.0792648228389228 0.23975497457784092 1.4795372543712351
		1.0792648228389228 -0.36072415203122243 1.579671119795941
		1.0792648228389228 -0.96120327864028698 1.4795372543712351
		1.0792648228389228 -1.4702649015799656 1.1943801313922568
		1.0792648228389228 -1.8104090034127782 0.76761233787681094
		1.0792648228389228 -1.9298517280486533 0.26420540172793361
		1.0792648228389228 -1.8104090034127782 -0.23920153442094003
		1.0792648228389228 -1.4702649015799627 -0.66596932793638908
		1.0792648228389228 -0.96120327864028632 -0.95112645091536463
		1.0792648228389228 -0.36072415203122238 -1.0512603163400724
		1.0792648228389228 0.23975497457784198 -0.95112645091536363
		1.0792648228389228 0.74881659751751306 -0.66596932793638763
		1.0792648228389228 1.0889606993503318 -0.23920153442093847
		1.0792648228389228 1.20840342398621 0.26420540172793322
		1.0792648228389228 1.0889606993503318 0.76761233787681094
		;
createNode nurbsCurve -n "ctrl_l_finMidBShape" -p "ctrl_l_finMidB";
	rename -uid "3A885021-45BD-37A2-6776-3EB337622360";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 6;
	setAttr ".cc" -type "nurbsCurve" 
		3 16 2 no 3
		21 -2 -1 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18
		19
		1.0792648228389321 1.4403698163283047 -0.50340693614885101
		1.0792648228389321 1.5699941000512569 2.19129498679071e-14
		1.0792648228389321 1.4403698163283047 0.50340693614889742
		1.0792648228389321 1.0712310873091966 0.93017472966434622
		1.0792648228389321 0.51877593823617241 1.2153318526433217
		1.0792648228389321 -0.13288934246278539 1.3154657180680358
		1.0792648228389321 -0.78455462316173075 1.2153318526433203
		1.0792648228389321 -1.3370097722347525 0.93017472966434622
		1.0792648228389321 -1.7061485012538651 0.50340693614889698
		1.0792648228389321 -1.8357727849768173 2.2125392644864728e-14
		1.0792648228389321 -1.7061485012538651 -0.50340693614885246
		1.0792648228389321 -1.3370097722347511 -0.93017472966429948
		1.0792648228389321 -0.78455462316173064 -1.2153318526432779
		1.0792648228389321 -0.13288934246278497 -1.3154657180679885
		1.0792648228389321 0.51877593823617352 -1.215331852643277
		1.0792648228389321 1.0712310873091966 -0.93017472966429948
		1.0792648228389321 1.4403698163283047 -0.50340693614885101
		1.0792648228389321 1.5699941000512569 2.19129498679071e-14
		1.0792648228389321 1.4403698163283047 0.50340693614889742
		;
createNode nurbsCurve -n "ctrl_l_finMidAShape" -p "ctrl_l_finMidA";
	rename -uid "CD204908-48E6-3696-974C-DB98623B2374";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 6;
	setAttr ".cc" -type "nurbsCurve" 
		1 17 0 no 3
		18 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17
		18
		9.8595418567213127 0.0030698631815791674 0.0014436059122514776
		9.918443859747951 0.003069863181579164 -0.29467660384204525
		10.100065838564683 0.0030698631815791488 -0.53183187810171406
		10.34473471008085 0.0030698631815791371 -0.69531438215289487
		10.633341322578655 0.0030698631815791184 -0.77235585994508871
		10.929461532332947 0.0030698631815790993 -0.71345385691844843
		11.180500158548202 0.0030698631815790842 -0.54571523005729983
		11.34823878540935 0.0030698631815790716 -0.29467660384204525
		11.407140788435987 0.003069863181579069 0.0014436059122513102
		11.330099310643792 0.0030698631815790742 0.29005021841004108
		11.166616806592616 0.0030698631815790876 0.53471908992621764
		10.929461532332947 0.0030698631815790993 0.716341068742952
		10.633341322578655 0.0030698631815791184 0.75560904079287061
		10.34473471008085 0.0030698631815791371 0.69820159397739745
		10.100065838564683 0.0030698631815791488 0.53471908992621764
		9.9365833345135091 0.0030698631815791631 0.29005021841004108
		9.8791758876980289 0.003069863181579164 0.0014436059122515138
		-0.20201566257708059 1.4210854715202004e-14 -7.1054273576010019e-15
		;
createNode transform -n "zero_l_finPinkyCarpal" -p "grp_l_finger";
	rename -uid "EEF28C40-4C7D-3286-89EA-E99267640D4C";
	setAttr ".t" -type "double3" -7.1054273576010019e-15 0 0 ;
	setAttr ".r" -type "double3" 1.4312496066585827e-14 -7.1562480332929104e-15 -1.8288189418415221e-14 ;
	setAttr ".s" -type "double3" 0.99999999999999933 1 1.0000000000000002 ;
createNode transform -n "ctrl_l_finPinkyCarpal" -p "zero_l_finPinkyCarpal";
	rename -uid "41E06923-47DE-32F8-F0AC-8985AE55CA9E";
	setAttr -k off -cb on ".v";
	setAttr ".t" -type "double3" -7.1054273576010019e-15 0 2.1316282072803006e-14 ;
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode nurbsCurve -n "ctrl_l_finPinkyCarpalShape" -p "ctrl_l_finPinkyCarpal";
	rename -uid "7AAF363F-4275-0619-F82F-7CA06F71A036";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 6;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		5.6733302949067044 1.7333575939009047 -3.0012273463898707
		4.280785372329837 1.7333575939009047 -2.9300120613538443
		2.8882404497529812 1.7333575939009047 -3.0012273463898698
		2.3656707760093871 1.7333575939009047 -2.2187940204783008
		2.8882404497529812 1.7333575939009047 -1.4363606945667304
		4.280785372329837 1.7333575939009047 -1.5075759796027559
		5.6733302949067044 1.7333575939009047 -1.4363606945667309
		6.1958999686502905 1.7333575939009047 -2.2187940204783008
		5.6733302949067044 1.7333575939009047 -3.0012273463898707
		4.280785372329837 1.7333575939009047 -2.9300120613538443
		2.8882404497529812 1.7333575939009047 -3.0012273463898698
		;
createNode transform -n "zero_l_finRingA" -p "grp_l_finger";
	rename -uid "4A4BC260-4D3B-79E4-3C94-D293CDA9DB54";
	setAttr ".t" -type "double3" 7.8236499382670388 -0.85799237357279878 -2.2971783733581432 ;
	setAttr ".r" -type "double3" -2.7955273647582977 15.005427888198101 -23.388524350159511 ;
	setAttr ".s" -type "double3" 1 1.0000000000000004 1 ;
createNode transform -n "driven_l_finRingA" -p "zero_l_finRingA";
	rename -uid "D3995246-4CE8-9293-BC51-0C8E9491F9A5";
	setAttr ".t" -type "double3" 6.0396132539608516e-14 0 1.6875389974302379e-14 ;
	setAttr ".r" -type "double3" 1.7393658414253607e-15 4.2738703532166022e-16 -1.319433231138381e-14 ;
createNode transform -n "ctrl_l_finRingA" -p "driven_l_finRingA";
	rename -uid "ED1157AD-4490-4287-5642-739BBF152AD3";
	addAttr -ci true -sn "fingerBent" -ln "fingerBent" -nn "��ָ����" -at "double";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 0 0 1.4210854715202004e-14 ;
	setAttr ".sp" -type "double3" 0 0 1.4210854715202004e-14 ;
	setAttr -av -k on ".fingerBent";
createNode transform -n "zero_l_finRingB" -p "ctrl_l_finRingA";
	rename -uid "595AA005-439E-BA3E-B8D2-5EA7AC69A5EC";
	setAttr ".t" -type "double3" 4.2513885498046733 1.4210854715202004e-14 -2.4868995751603507e-14 ;
	setAttr ".r" -type "double3" 0 0 -25.589432634615694 ;
	setAttr ".s" -type "double3" 1.0000000000000004 1.0000000000000004 0.99999999999999967 ;
createNode transform -n "offset_l_finRingB" -p "zero_l_finRingB";
	rename -uid "564D2307-4392-25F2-D505-A2B0B7A0D266";
	setAttr ".t" -type "double3" 2.8421709430404007e-14 -1.4210854715202004e-14 8.8817841970012523e-16 ;
	setAttr ".s" -type "double3" 0.99999999999999989 0.99999999999999978 0.99999999999999989 ;
createNode transform -n "ctrl_l_finRingB" -p "offset_l_finRingB";
	rename -uid "192FBD97-4C37-6E9D-A961-F297FDC258C6";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 0 -3.5527136788005001e-15 3.5527136788005001e-15 ;
	setAttr ".sp" -type "double3" 0 -3.5527136788005009e-15 3.5527136788005009e-15 ;
	setAttr ".spt" -type "double3" 0 7.8886090522101163e-31 -7.8886090522101163e-31 ;
createNode transform -n "zero_l_finRingC" -p "ctrl_l_finRingB";
	rename -uid "1CE0EB15-4355-B64E-6BB1-C681D4551178";
	setAttr ".t" -type "double3" 3.2332154594604248 7.1054273576010019e-15 7.1054273576010019e-15 ;
	setAttr ".r" -type "double3" 0 0 -11.213505447688787 ;
	setAttr ".s" -type "double3" 0.99999999999999956 0.99999999999999989 1 ;
createNode transform -n "offset_l_finRingC" -p "zero_l_finRingC";
	rename -uid "77B56BDE-4F54-D416-81D2-BAB2483E5C72";
	setAttr ".t" -type "double3" 2.8421709430404007e-14 -1.4210854715202004e-14 8.8817841970012523e-16 ;
	setAttr ".s" -type "double3" 0.99999999999999989 0.99999999999999978 0.99999999999999989 ;
createNode transform -n "ctrl_l_finRingC" -p "offset_l_finRingC";
	rename -uid "1136ADF5-41B6-CD63-DEE9-65B31BFD3FE7";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 0 -3.5527136788005001e-15 3.5527136788005001e-15 ;
	setAttr ".sp" -type "double3" 0 -3.5527136788005009e-15 3.5527136788005009e-15 ;
	setAttr ".spt" -type "double3" 0 7.8886090522101163e-31 -7.8886090522101163e-31 ;
createNode nurbsCurve -n "ctrl_l_finRingCShape" -p "ctrl_l_finRingC";
	rename -uid "FDDB4CB9-4FE8-9EBC-49A7-1F8D25502AEE";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 6;
	setAttr ".cc" -type "nurbsCurve" 
		3 16 2 no 3
		21 -2 -1 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18
		19
		1.0792648228389228 1.1037400772921984 -0.45357209422660794
		1.0792648228389228 1.2061546907378777 2.6841512194774214e-14
		1.0792648228389228 1.1037400772921984 0.4535720942266589
		1.0792648228389228 0.81208793346148045 0.83809194874855653
		1.0792648228389228 0.37559965431068931 1.0950199013959256
		1.0792648228389228 -0.13927337643557686 1.1852410004358924
		1.0792648228389228 -0.65414640718183958 1.0950199013959254
		1.0792648228389228 -1.0906346863326317 0.83809194874855653
		1.0792648228389228 -1.3822868301633464 0.45357209422665873
		1.0792648228389228 -1.4847014436090242 2.703292416852475e-14
		1.0792648228389228 -1.3822868301633464 -0.45357209422660916
		1.0792648228389228 -1.0906346863326317 -0.83809194874851345
		1.0792648228389228 -0.65414640718183925 -1.0950199013958868
		1.0792648228389228 -0.13927337643557652 -1.1852410004358511
		1.0792648228389228 0.37559965431068965 -1.0950199013958868
		1.0792648228389228 0.81208793346148045 -0.83809194874851323
		1.0792648228389228 1.1037400772921984 -0.45357209422660794
		1.0792648228389228 1.2061546907378777 2.6841512194774214e-14
		1.0792648228389228 1.1037400772921984 0.4535720942266589
		;
createNode nurbsCurve -n "ctrl_l_finRingBShape" -p "ctrl_l_finRingB";
	rename -uid "6F0077CB-42DA-525D-0655-44B61AC14767";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 6;
	setAttr ".cc" -type "nurbsCurve" 
		3 16 2 no 3
		21 -2 -1 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18
		19
		1.0792648228389254 1.4484218468529018 -0.51020120685708514
		1.0792648228389254 1.5677605097666907 2.188177667980434e-14
		1.0792648228389254 1.4484218468529018 0.51020120685712744
		1.0792648228389254 1.1085740877324932 0.94272890495569761
		1.0792648228389254 0.59995597300393511 1.2317346731335679
		1.0792648228389254 -3.8032284666808897e-14 1.3332200030294745
		1.0792648228389254 -0.59995597300400094 1.2317346731335679
		1.0792648228389254 -1.1085740877325463 0.94272890495569761
		1.0792648228389254 -1.4484218468529493 0.51020120685712678
		1.0792648228389254 -1.5677605097667373 2.2097086707157063e-14
		1.0792648228389254 -1.4484218468529493 -0.51020120685708514
		1.0792648228389254 -1.1085740877325447 -0.94272890495565176
		1.0792648228389254 -0.59995597300400039 -1.2317346731335226
		1.0792648228389254 -3.7690634233154026e-14 -1.3332200030294292
		1.0792648228389254 0.59995597300393533 -1.2317346731335224
		1.0792648228389254 1.1085740877324932 -0.94272890495565143
		1.0792648228389254 1.4484218468529018 -0.51020120685708514
		1.0792648228389254 1.5677605097666907 2.188177667980434e-14
		1.0792648228389254 1.4484218468529018 0.51020120685712744
		;
createNode nurbsCurve -n "ctrl_l_finRingAShape" -p "ctrl_l_finRingA";
	rename -uid "69CFA131-4C7A-68AF-4275-B9AC0ABC5DEC";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 6;
	setAttr ".cc" -type "nurbsCurve" 
		1 17 0 no 3
		18 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17
		18
		9.8595418567213127 0.0030698631815791674 0.0014436059122514776
		9.918443859747951 0.003069863181579164 -0.29467660384204525
		10.100065838564683 0.0030698631815791488 -0.53183187810171406
		10.34473471008085 0.0030698631815791371 -0.69531438215289487
		10.633341322578655 0.0030698631815791184 -0.77235585994508871
		10.929461532332947 0.0030698631815790993 -0.71345385691844843
		11.180500158548202 0.0030698631815790842 -0.54571523005729983
		11.34823878540935 0.0030698631815790716 -0.29467660384204525
		11.407140788435987 0.003069863181579069 0.0014436059122513102
		11.330099310643792 0.0030698631815790742 0.29005021841004108
		11.166616806592616 0.0030698631815790876 0.53471908992621764
		10.929461532332947 0.0030698631815790993 0.716341068742952
		10.633341322578655 0.0030698631815791184 0.75560904079287061
		10.34473471008085 0.0030698631815791371 0.69820159397739745
		10.100065838564683 0.0030698631815791488 0.53471908992621764
		9.9365833345135091 0.0030698631815791631 0.29005021841004108
		9.8791758876980289 0.003069863181579164 0.0014436059122515138
		-0.20201566257708059 1.4210854715202004e-14 -7.1054273576010019e-15
		;
createNode transform -n "zero_l_finPinkyA" -p "grp_l_finger";
	rename -uid "417CCDAE-42E6-8C98-A617-97BA662E5642";
	setAttr ".t" -type "double3" 6.9648748283412161 -1.4394202278004258 -4.150163666610176 ;
	setAttr ".r" -type "double3" -10.765994754653926 21.924917623264221 -26.934022494441265 ;
	setAttr ".s" -type "double3" 1.0000000000000002 1.0000000000000002 1 ;
createNode transform -n "driven_l_finPinkyA" -p "zero_l_finPinkyA";
	rename -uid "F83EEF80-4448-1B4C-2BE6-0EAD5B3D5873";
	setAttr ".t" -type "double3" 6.0396132539608516e-14 0 1.6875389974302379e-14 ;
	setAttr ".r" -type "double3" 1.7393658414253607e-15 4.2738703532166022e-16 -1.319433231138381e-14 ;
createNode transform -n "ctrl_l_finPinkyA" -p "driven_l_finPinkyA";
	rename -uid "912C9B70-4439-7C43-401C-6F858F521840";
	addAttr -ci true -sn "fingerBent" -ln "fingerBent" -nn "��ָ����" -at "double";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 0 0 1.4210854715202004e-14 ;
	setAttr ".sp" -type "double3" 0 0 1.4210854715202004e-14 ;
	setAttr -av -k on ".fingerBent";
createNode transform -n "zero_l_finPinkyB" -p "ctrl_l_finPinkyA";
	rename -uid "7C78A2EF-43A9-F1C6-5EC4-0C831B998DAD";
	setAttr ".t" -type "double3" 2.8932974338531352 2.8421709430404007e-14 -3.1974423109204508e-14 ;
	setAttr ".r" -type "double3" 0 0 -20.287369680429229 ;
	setAttr ".s" -type "double3" 1.0000000000000004 1.0000000000000004 0.99999999999999956 ;
createNode transform -n "offset_l_finPinkyB" -p "zero_l_finPinkyB";
	rename -uid "0279F694-4827-7631-B592-52AA6D3480A6";
	setAttr ".t" -type "double3" 2.8421709430404007e-14 -1.4210854715202004e-14 8.8817841970012523e-16 ;
	setAttr ".s" -type "double3" 0.99999999999999989 0.99999999999999978 0.99999999999999989 ;
createNode transform -n "ctrl_l_finPinkyB" -p "offset_l_finPinkyB";
	rename -uid "01116363-47A8-1C13-7071-8D8D11DD7323";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 0 -3.5527136788005001e-15 3.5527136788005001e-15 ;
	setAttr ".sp" -type "double3" 0 -3.5527136788005009e-15 3.5527136788005009e-15 ;
	setAttr ".spt" -type "double3" 0 7.8886090522101163e-31 -7.8886090522101163e-31 ;
createNode transform -n "zero_l_finPinkyC" -p "ctrl_l_finPinkyB";
	rename -uid "8E920DB8-4498-7067-44DA-22A2FA29833A";
	setAttr ".t" -type "double3" 1.7904913688182376 -7.1054273576010019e-15 -3.5527136788005009e-15 ;
	setAttr ".r" -type "double3" 0 0 -15.448097595578739 ;
	setAttr ".s" -type "double3" 0.99999999999999911 0.99999999999999933 1 ;
createNode transform -n "offset_l_finPinkyC" -p "zero_l_finPinkyC";
	rename -uid "832E7B30-4E70-999A-24BA-2EAD5BA1D307";
	setAttr ".t" -type "double3" 2.8421709430404007e-14 -1.4210854715202004e-14 8.8817841970012523e-16 ;
	setAttr ".s" -type "double3" 0.99999999999999989 0.99999999999999978 0.99999999999999989 ;
createNode transform -n "ctrl_l_finPinkyC" -p "offset_l_finPinkyC";
	rename -uid "B287B54A-4421-8179-BD28-A987533A9233";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 0 -3.5527136788005001e-15 3.5527136788005001e-15 ;
	setAttr ".sp" -type "double3" 0 -3.5527136788005009e-15 3.5527136788005009e-15 ;
	setAttr ".spt" -type "double3" 0 7.8886090522101163e-31 -7.8886090522101163e-31 ;
createNode nurbsCurve -n "ctrl_l_finPinkyCShape" -p "ctrl_l_finPinkyC";
	rename -uid "C2DB6183-43C5-011F-E23E-9C81F300975E";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 6;
	setAttr ".cc" -type "nurbsCurve" 
		3 16 2 no 3
		21 -2 -1 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18
		19
		1.0792648228389228 1.1037400772921984 -0.45357209422660794
		1.0792648228389228 1.2061546907378777 2.6841512194774214e-14
		1.0792648228389228 1.1037400772921984 0.4535720942266589
		1.0792648228389228 0.81208793346148045 0.83809194874855653
		1.0792648228389228 0.37559965431068931 1.0950199013959256
		1.0792648228389228 -0.13927337643557686 1.1852410004358924
		1.0792648228389228 -0.65414640718183958 1.0950199013959254
		1.0792648228389228 -1.0906346863326317 0.83809194874855653
		1.0792648228389228 -1.3822868301633464 0.45357209422665873
		1.0792648228389228 -1.4847014436090242 2.703292416852475e-14
		1.0792648228389228 -1.3822868301633464 -0.45357209422660916
		1.0792648228389228 -1.0906346863326317 -0.83809194874851345
		1.0792648228389228 -0.65414640718183925 -1.0950199013958868
		1.0792648228389228 -0.13927337643557652 -1.1852410004358511
		1.0792648228389228 0.37559965431068965 -1.0950199013958868
		1.0792648228389228 0.81208793346148045 -0.83809194874851323
		1.0792648228389228 1.1037400772921984 -0.45357209422660794
		1.0792648228389228 1.2061546907378777 2.6841512194774214e-14
		1.0792648228389228 1.1037400772921984 0.4535720942266589
		;
createNode nurbsCurve -n "ctrl_l_finPinkyBShape" -p "ctrl_l_finPinkyB";
	rename -uid "6C334B06-41F3-F883-35C0-DA95F71E601D";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 6;
	setAttr ".cc" -type "nurbsCurve" 
		3 16 2 no 3
		21 -2 -1 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18
		19
		1.0792648228389254 1.4484218468529018 -0.51020120685708514
		1.0792648228389254 1.5677605097666907 2.188177667980434e-14
		1.0792648228389254 1.4484218468529018 0.51020120685712744
		1.0792648228389254 1.1085740877324932 0.94272890495569761
		1.0792648228389254 0.59995597300393511 1.2317346731335679
		1.0792648228389254 -3.8032284666808897e-14 1.3332200030294745
		1.0792648228389254 -0.59995597300400094 1.2317346731335679
		1.0792648228389254 -1.1085740877325463 0.94272890495569761
		1.0792648228389254 -1.4484218468529493 0.51020120685712678
		1.0792648228389254 -1.5677605097667373 2.2097086707157063e-14
		1.0792648228389254 -1.4484218468529493 -0.51020120685708514
		1.0792648228389254 -1.1085740877325447 -0.94272890495565176
		1.0792648228389254 -0.59995597300400039 -1.2317346731335226
		1.0792648228389254 -3.7690634233154026e-14 -1.3332200030294292
		1.0792648228389254 0.59995597300393533 -1.2317346731335224
		1.0792648228389254 1.1085740877324932 -0.94272890495565143
		1.0792648228389254 1.4484218468529018 -0.51020120685708514
		1.0792648228389254 1.5677605097666907 2.188177667980434e-14
		1.0792648228389254 1.4484218468529018 0.51020120685712744
		;
createNode nurbsCurve -n "ctrl_l_finPinkyAShape" -p "ctrl_l_finPinkyA";
	rename -uid "8D684C6E-42D1-AFF0-2418-CABCFCA01448";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 6;
	setAttr ".cc" -type "nurbsCurve" 
		1 17 0 no 3
		18 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17
		18
		9.8595418567213127 0.0030698631815791674 0.0014436059122514776
		9.918443859747951 0.003069863181579164 -0.29467660384204525
		10.100065838564683 0.0030698631815791488 -0.53183187810171406
		10.34473471008085 0.0030698631815791371 -0.69531438215289487
		10.633341322578655 0.0030698631815791184 -0.77235585994508871
		10.929461532332947 0.0030698631815790993 -0.71345385691844843
		11.180500158548202 0.0030698631815790842 -0.54571523005729983
		11.34823878540935 0.0030698631815790716 -0.29467660384204525
		11.407140788435987 0.003069863181579069 0.0014436059122513102
		11.330099310643792 0.0030698631815790742 0.29005021841004108
		11.166616806592616 0.0030698631815790876 0.53471908992621764
		10.929461532332947 0.0030698631815790993 0.716341068742952
		10.633341322578655 0.0030698631815791184 0.75560904079287061
		10.34473471008085 0.0030698631815791371 0.69820159397739745
		10.100065838564683 0.0030698631815791488 0.53471908992621764
		9.9365833345135091 0.0030698631815791631 0.29005021841004108
		9.8791758876980289 0.003069863181579164 0.0014436059122515138
		-0.20201566257708059 1.4210854715202004e-14 -7.1054273576010019e-15
		;
createNode transform -n "zero_l_armIkFkText" -p "grp_l_arm";
	rename -uid "B9AB46DF-4F81-B457-EAB6-A1B28B174A5A";
	setAttr ".t" -type "double3" 41.701575911231174 115.30155509980524 7.7564333597989572 ;
	setAttr ".r" -type "double3" -36.630301520957502 5.1812178916657278e-05 37.113548848248506 ;
	setAttr ".s" -type "double3" 1 1.0000000000000002 1.0000000000000002 ;
createNode transform -n "driven_l_armIkFkText" -p "zero_l_armIkFkText";
	rename -uid "62430049-4EAC-47EC-7499-0AB0CC39BC59";
	setAttr ".t" -type "double3" 2.1316282072803006e-14 1.7763568394002505e-14 -1.4210854715202004e-14 ;
	setAttr ".s" -type "double3" 1.0000000000000007 1 1.0000000000000002 ;
createNode transform -n "crv_l_armIkFkText" -p "driven_l_armIkFkText";
	rename -uid "8F14F674-4F4F-1BC7-7780-60BD15FCF68E";
createNode nurbsCurve -n "crv_l_armIkFkTextShape" -p "crv_l_armIkFkText";
	rename -uid "ED73793E-484C-1D78-9847-48A0210B0F42";
	setAttr -k off ".v";
	setAttr ".ovdt" 2;
	setAttr ".ove" yes;
	setAttr ".ovc" 1;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-0.018149999901652336 1.0813100337982176 -0.84135001897811912
		-0.018149999901652336 0.81077998876571633 -0.84135001897811912
		-0.018149999901652336 0.81077998876571677 1.0413500070571897
		-0.018149999901652336 1.081310033798218 1.0413500070571897
		-0.018149999901652336 1.0813100337982176 -0.84135001897811912
		;
createNode nurbsCurve -n "crv_l_armIkFkTextShape1" -p "crv_l_armIkFkText";
	rename -uid "044F98EA-44F0-C823-2B67-668469A66A8C";
	setAttr -k off ".v";
	setAttr ".ovdt" 2;
	setAttr ".ove" yes;
	setAttr ".ovc" 1;
	setAttr ".cc" -type "nurbsCurve" 
		1 11 0 no 3
		12 0 1 2 3 4 5 6 7 8 9 10 11
		12
		-0.018149999901652336 0.39393997192382796 -0.84135001897811901
		-0.018149999901652336 0.39393997192382835 1.0413500070571899
		-0.018149999901652336 0.12340000271797204 1.0413500070571899
		-0.018149999901652336 0.12340000271797183 0.11103999614715573
		-0.018149999901652336 -0.83451002836227395 1.0413500070571902
		-0.018149999901652336 -1.2071800231933592 1.0413500070571902
		-0.018149999901652336 -0.18578000366687775 0.05031000077724461
		-0.018149999901652336 -1.0056600570678713 -0.84135001897811867
		-0.018149999901652336 -0.66886997222900413 -0.84135001897811879
		-0.018149999901652336 0.1234000027179718 0.019940000027418109
		-0.018149999901652336 0.12340000271797162 -0.8413500189781189
		-0.018149999901652336 0.39393997192382796 -0.84135001897811901
		;
createNode nurbsCurve -n "crv_l_armIkFkTextShape2" -p "crv_l_armIkFkText";
	rename -uid "FA2E0374-4969-E3E5-25DE-2D95B3B71D34";
	setAttr -k off ".v";
	setAttr ".ovdt" 2;
	setAttr ".ove" yes;
	setAttr ".ovc" 1;
	setAttr ".cc" -type "nurbsCurve" 
		1 10 0 no 3
		11 0 1 2 3 4 5 6 7 8 9 10
		11
		-0.018149999901652336 -3.2946801185607906 1.0413500070571906
		-0.018149999901652336 -3.294680118560791 -0.84135001897811812
		-0.018149999901652336 -4.2995200157165527 -0.8413500189781179
		-0.018149999901652336 -4.2995200157165527 -0.59842002391815086
		-0.018149999901652336 -3.5652101039886475 -0.59842002391815108
		-0.018149999901652336 -3.5652101039886475 -0.076680004596709414
		-0.018149999901652336 -4.2995200157165527 -0.076680004596709248
		-0.018149999901652336 -4.2995200157165527 0.16625000536441897
		-0.018149999901652336 -3.5652101039886475 0.16625000536441883
		-0.018149999901652336 -3.565210103988647 1.0413500070571908
		-0.018149999901652336 -3.2946801185607906 1.0413500070571906
		;
createNode nurbsCurve -n "crv_l_armIkFkTextShape3" -p "crv_l_armIkFkText";
	rename -uid "7EA55E5E-4147-CA17-9CB9-028C3D276698";
	setAttr -k off ".v";
	setAttr ".ovdt" 2;
	setAttr ".ove" yes;
	setAttr ".ovc" 1;
	setAttr ".cc" -type "nurbsCurve" 
		1 11 0 no 3
		12 0 1 2 3 4 5 6 7 8 9 10 11
		12
		-0.018149999901652336 -4.5866098403930664 -0.8413500189781179
		-0.018149999901652336 -4.5866098403930664 1.0413500070571911
		-0.018149999901652336 -4.8571500778198242 1.0413500070571911
		-0.018149999901652336 -4.8571500778198242 0.11103999614715684
		-0.018149999901652336 -5.8150601387023926 1.0413500070571913
		-0.018149999901652336 -6.1877298355102539 1.0413500070571913
		-0.018149999901652336 -5.1663298606872559 0.050310000777245713
		-0.018149999901652336 -5.9862098693847656 -0.84135001897811756
		-0.018149999901652336 -5.6494302749633789 -0.84135001897811768
		-0.018149999901652336 -4.8571500778198242 0.019940000027419216
		-0.018149999901652336 -4.8571500778198242 -0.84135001897811779
		-0.018149999901652336 -4.5866098403930664 -0.8413500189781179
		;
createNode transform -n "zero_l_armBlendIkFk" -p "crv_l_armIkFkText";
	rename -uid "B2AF035F-4581-51D2-7B85-E9842ADDC407";
	setAttr ".ove" yes;
	setAttr ".ovc" 20;
createNode transform -n "ctrl_l_armBlendIkFk" -p "zero_l_armBlendIkFk";
	rename -uid "0D94774C-4D2D-1102-18C3-F48C5C86F32B";
	addAttr -ci true -sn "ikFkVis" -ln "ikFkVis" -nn "IKFK�������л���ʾ" -min 0 -max 
		1 -at "bool";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".mntl" -type "double3" -1 -4.7 -1 ;
	setAttr ".mxtl" -type "double3" 1 0 1 ;
	setAttr ".mtye" yes;
	setAttr ".xtye" yes;
	setAttr -cb on ".ikFkVis";
createNode nurbsCurve -n "ctrl_l_armBlendIkFkShape" -p "ctrl_l_armBlendIkFk";
	rename -uid "B845A597-4226-EA3A-FDE1-89A765A3860A";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 6;
	setAttr ".cc" -type "nurbsCurve" 
		1 34 0 no 3
		35 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
		 28 29 30 31 32 33 34
		35
		-3.8239900135295102e-08 -2.1665270093824187 1.1834709834346313e-07
		-4.8990717260721794e-08 -2.1412579207524125 0.25656045714332465
		0 -2.066422173651322 0.50326126434805163
		-4.8990717260721794e-08 -1.944894543135101 0.73062204209010162
		0 -1.7813471304577746 0.92990549942973633
		0 -1.5820634758554419 1.0934529778612954
		0 -1.3547023693422293 1.2149798193267229
		0 -1.1080016278917348 1.2898153034108828
		9.798169742225582e-08 -0.85144110499417636 1.3150842605324224
		9.798169742225582e-08 0.85144110499417636 1.3150842605324224
		0 1.1080016278917348 1.2898153034108828
		0 1.3547023693422275 1.2149798193267229
		0 1.5820634758554419 1.0934529778612954
		0 1.7813471304577746 0.92990549942973633
		-4.8990717260721794e-08 1.9448945431351028 0.73062204209010162
		0 2.066422173651322 0.50326126434805163
		-4.8990717260721794e-08 2.1412579207524125 0.25656045714332465
		-3.8239900135295102e-08 2.1665270093824169 1.1834709834346313e-07
		-4.8990717260721794e-08 2.1412579207524125 -0.25656025988062647
		-4.8990717260721794e-08 2.066422173651322 -0.50326126434805163
		0 1.9448953321858937 -0.73062184482740333
		0 1.7813479195085691 -0.92990549942973644
		0 1.5820643306604687 -1.0934529778612951
		0 1.354703158393022 -1.2149798193267229
		0 1.1080023511882935 -1.2898156321820462
		0 0.85144222281613402 -1.3150846550578188
		0 -0.85144222281613402 -1.3150846550578188
		0 -1.1080023511882953 -1.2898156321820462
		0 -1.354703158393022 -1.2149798193267229
		0 -1.5820643306604687 -1.0934529778612951
		0 -1.7813479195085691 -0.92990549942973644
		0 -1.9448953321858937 -0.73062184482740333
		-4.8990717260721794e-08 -2.066422173651322 -0.50326126434805163
		-4.8990717260721794e-08 -2.1412579207524125 -0.25656025988062647
		-3.8239900135295102e-08 -2.1665270093824187 1.1834709834346313e-07
		;
createNode lightLinker -s -n "lightLinker1";
	rename -uid "9FC909A5-42E3-D49E-97AA-CCA9DD708A66";
	setAttr -s 2 ".lnk";
	setAttr -s 2 ".slnk";
createNode shapeEditorManager -n "shapeEditorManager";
	rename -uid "089D4A34-45AB-1A51-7964-B58AB67C1265";
createNode poseInterpolatorManager -n "poseInterpolatorManager";
	rename -uid "33E0CFD5-4F76-E9FD-2530-149D32706B34";
createNode displayLayerManager -n "layerManager";
	rename -uid "26637625-453B-A79A-295B-D19F7060EA36";
	setAttr ".cdl" 2;
	setAttr -s 3 ".dli[1:2]"  2 3;
createNode displayLayer -n "defaultLayer";
	rename -uid "46019A56-4C2E-AF1B-9D7A-26A74781CDA9";
createNode renderLayerManager -n "renderLayerManager";
	rename -uid "6A2B89F3-48E8-22EA-E4D7-B1AADD13C1B8";
createNode renderLayer -n "defaultRenderLayer";
	rename -uid "487210EB-41F3-029F-CBF7-D78F6F8C4A04";
	setAttr ".g" yes;
createNode nodeGraphEditorInfo -n "_hyperShadePrimaryNodeEditorSavedTabsInfo";
	rename -uid "46A64B96-4FEA-67C1-ECD4-86B169B23207";
	setAttr ".def" no;
	setAttr ".tgi[0].tn" -type "string" "�ޱ���_1";
	setAttr ".tgi[0].vl" -type "double2" -504.76188470446959 -315.4761779402935 ;
	setAttr ".tgi[0].vh" -type "double2" 483.33331412739307 328.57141551517361 ;
createNode connectionOverride -n "_connectionOverride1";
	rename -uid "D5D49738-4EAA-2B7A-8C91-04B304C0CE28";
createNode nodeGraphEditorInfo -n "_hyperShadePrimaryNodeEditorSavedTabsInfo1";
	rename -uid "334277CA-4EEE-97FA-BBC1-C7B652AC08EF";
	setAttr ".def" no;
	setAttr ".tgi[0].tn" -type "string" "�ޱ���_1";
	setAttr ".tgi[0].vl" -type "double2" -885.12907280935133 -455.95236283446201 ;
	setAttr ".tgi[0].vh" -type "double2" 868.46240680495839 469.04760040934195 ;
createNode nodeGraphEditorInfo -n "control_hyperShadePrimaryNodeEditorSavedTabsInfo";
	rename -uid "F3FFD2AC-4021-F440-6478-F0B5FC23A07A";
	setAttr ".def" no;
	setAttr ".tgi[0].tn" -type "string" "�ޱ���_1";
	setAttr ".tgi[0].vl" -type "double2" -218.02247810905186 -215.07935653287933 ;
	setAttr ".tgi[0].vh" -type "double2" 214.8478750605961 221.42856262979089 ;
createNode nodeGraphEditorInfo -n "pasted___hyperShadePrimaryNodeEditorSavedTabsInfo";
	rename -uid "EBBF4E18-4C01-A66D-66E2-EB8BA4CEBDA3";
	setAttr ".def" no;
	setAttr ".tgi[0].tn" -type "string" "�ޱ���_1";
	setAttr ".tgi[0].vl" -type "double2" -504.76188470446959 -315.4761779402935 ;
	setAttr ".tgi[0].vh" -type "double2" 483.33331412739307 328.57141551517361 ;
createNode connectionOverride -n "pasted___connectionOverride1";
	rename -uid "6946D250-42AF-7ABE-E104-7A866C257157";
createNode nodeGraphEditorInfo -n "pasted___hyperShadePrimaryNodeEditorSavedTabsInfo1";
	rename -uid "76717316-4137-7644-35DF-A9A652F0242A";
	setAttr ".def" no;
	setAttr ".tgi[0].tn" -type "string" "�ޱ���_1";
	setAttr ".tgi[0].vl" -type "double2" -885.12907280935133 -455.95236283446201 ;
	setAttr ".tgi[0].vh" -type "double2" 868.46240680495839 469.04760040934195 ;
createNode nodeGraphEditorInfo -n "pasted__hyperShadePrimaryNodeEditorSavedTabsInfo";
	rename -uid "F32F35C0-4255-D7B9-DB72-67981E28124F";
	setAttr ".def" no;
	setAttr ".tgi[0].tn" -type "string" "�ޱ���_1";
	setAttr ".tgi[0].vl" -type "double2" -218.02247810905186 -215.07935653287933 ;
	setAttr ".tgi[0].vh" -type "double2" 214.8478750605961 221.42856262979089 ;
createNode nodeGraphEditorInfo -n "hyperShadePrimaryNodeEditorSavedTabsInfo1";
	rename -uid "86D87C49-4082-EEE7-6ACD-8888B42612D1";
	setAttr ".def" no;
	setAttr ".tgi[0].tn" -type "string" "�ޱ���_1";
	setAttr ".tgi[0].vl" -type "double2" -334.92062161208514 -328.57141551517361 ;
	setAttr ".tgi[0].vh" -type "double2" 326.19046322883179 338.09522466054091 ;
createNode nodeGraphEditorInfo -n "hyperShadePrimaryNodeEditorSavedTabsInfo3";
	rename -uid "1D7C8C4D-4E5E-673B-8D35-C294048A7547";
	setAttr ".def" no;
	setAttr ".tgi[0].tn" -type "string" "�ޱ���_1";
	setAttr ".tgi[0].vl" -type "double2" -330.95236780151544 -320.2380825129772 ;
	setAttr ".tgi[0].vh" -type "double2" 317.85713022663526 333.33332008785726 ;
createNode nodeGraphEditorInfo -n "hyperShadePrimaryNodeEditorSavedTabsInfo";
	rename -uid "8DF7BE8A-4D2C-0DB2-5A60-92BCEA338DEB";
	setAttr ".def" no;
	setAttr ".tgi[0].tn" -type "string" "�ޱ���_1";
	setAttr ".tgi[0].vl" -type "double2" -114.48622045432295 -199.99999205271436 ;
	setAttr ".tgi[0].vh" -type "double2" 746.62905247808089 358.33331909444655 ;
createNode decomposeMatrix -n "dec_l_armPv";
	rename -uid "649EC8D8-4168-EE66-A1F9-498EA162DADB";
createNode remapValue -n "rem_l_armBlendIkFk";
	rename -uid "B25172D2-4B6C-0AA3-9364-50A7A79451F6";
	setAttr ".imn" -4.6999998092651367;
	setAttr ".imx" 0;
	setAttr -s 2 ".vl[0:1]"  0 0 1 1 1 1;
	setAttr -s 2 ".cl";
	setAttr ".cl[0].clp" 0;
	setAttr ".cl[0].clc" -type "float3" 0 0 0 ;
	setAttr ".cl[0].cli" 1;
	setAttr ".cl[1].clp" 1;
	setAttr ".cl[1].clc" -type "float3" 1 1 1 ;
	setAttr ".cl[1].cli" 1;
createNode reverse -n "rev_l_armBlendIkFk";
	rename -uid "7BC66C89-428D-1896-C281-3AA3DDFBFAD1";
createNode addDoubleLinear -n "add_l_armIk";
	rename -uid "C2A4BF76-4B26-935F-5800-B98C116EA22E";
	setAttr ".ihi" 2;
createNode addDoubleLinear -n "add_l_armFk";
	rename -uid "B7075484-4384-E3EF-C422-F69670719FF9";
	setAttr ".ihi" 2;
createNode nodeGraphEditorInfo -n "control__hyperShadePrimaryNodeEditorSavedTabsInfo";
	rename -uid "AE5C782D-41CD-948A-9101-518C895EB411";
	setAttr ".def" no;
	setAttr ".tgi[0].tn" -type "string" "�ޱ���_1";
	setAttr ".tgi[0].vl" -type "double2" -504.76188470446959 -315.4761779402935 ;
	setAttr ".tgi[0].vh" -type "double2" 483.33331412739307 328.57141551517361 ;
createNode decomposeMatrix -n "dec_l_forearmIk";
	rename -uid "3091AC91-4956-55DB-7EF1-A69738ECB085";
createNode connectionOverride -n "control__connectionOverride1";
	rename -uid "03220386-49F8-755D-9906-CA9B7F088014";
createNode nodeGraphEditorInfo -n "control__hyperShadePrimaryNodeEditorSavedTabsInfo1";
	rename -uid "3587815C-4974-C948-CE34-29A8CC3CEF99";
	setAttr ".def" no;
	setAttr ".tgi[0].tn" -type "string" "�ޱ���_1";
	setAttr ".tgi[0].vl" -type "double2" -885.12907280935133 -455.95236283446201 ;
	setAttr ".tgi[0].vh" -type "double2" 868.46240680495839 469.04760040934195 ;
createNode nodeGraphEditorInfo -n "control_control_hyperShadePrimaryNodeEditorSavedTabsInfo";
	rename -uid "74101E27-43D8-E882-D30D-699456636DEF";
	setAttr ".def" no;
	setAttr ".tgi[0].tn" -type "string" "�ޱ���_1";
	setAttr ".tgi[0].vl" -type "double2" -218.02247810905186 -215.07935653287933 ;
	setAttr ".tgi[0].vh" -type "double2" 214.8478750605961 221.42856262979089 ;
createNode nodeGraphEditorInfo -n "control_pasted___hyperShadePrimaryNodeEditorSavedTabsInfo";
	rename -uid "09351BD5-48A1-760A-3890-EEBCA8FA4E81";
	setAttr ".def" no;
	setAttr ".tgi[0].tn" -type "string" "�ޱ���_1";
	setAttr ".tgi[0].vl" -type "double2" -504.76188470446959 -315.4761779402935 ;
	setAttr ".tgi[0].vh" -type "double2" 483.33331412739307 328.57141551517361 ;
createNode connectionOverride -n "control_pasted___connectionOverride1";
	rename -uid "0F1F8BD0-48DE-BC36-E75B-E087C8C34190";
createNode nodeGraphEditorInfo -n "control_pasted___hyperShadePrimaryNodeEditorSavedTabsInfo1";
	rename -uid "F90F6D53-41B8-3842-F886-FD91DB9382F0";
	setAttr ".def" no;
	setAttr ".tgi[0].tn" -type "string" "�ޱ���_1";
	setAttr ".tgi[0].vl" -type "double2" -885.12907280935133 -455.95236283446201 ;
	setAttr ".tgi[0].vh" -type "double2" 868.46240680495839 469.04760040934195 ;
createNode nodeGraphEditorInfo -n "control_pasted__hyperShadePrimaryNodeEditorSavedTabsInfo";
	rename -uid "D927FBB9-41E8-CB55-A2D1-72B2396AC775";
	setAttr ".def" no;
	setAttr ".tgi[0].tn" -type "string" "�ޱ���_1";
	setAttr ".tgi[0].vl" -type "double2" -218.02247810905186 -215.07935653287933 ;
	setAttr ".tgi[0].vh" -type "double2" 214.8478750605961 221.42856262979089 ;
createNode nodeGraphEditorInfo -n "control_hyperShadePrimaryNodeEditorSavedTabsInfo2";
	rename -uid "CCDE098E-46A4-57A6-8E12-9A9FB67AE3BE";
	setAttr ".def" no;
	setAttr ".tgi[0].tn" -type "string" "�ޱ���_1";
	setAttr ".tgi[0].vl" -type "double2" -334.92062161208514 -328.57141551517361 ;
	setAttr ".tgi[0].vh" -type "double2" 326.19046322883179 338.09522466054091 ;
createNode nodeGraphEditorInfo -n "control_hyperShadePrimaryNodeEditorSavedTabsInfo3";
	rename -uid "E930240C-480E-BDD5-DDFE-40BBBFC54627";
	setAttr ".def" no;
	setAttr ".tgi[0].tn" -type "string" "�ޱ���_1";
	setAttr ".tgi[0].vl" -type "double2" -330.95236780151544 -320.2380825129772 ;
	setAttr ".tgi[0].vh" -type "double2" 317.85713022663526 333.33332008785726 ;
createNode unitConversion -n "unitConversion159";
	rename -uid "72CBAAFF-4467-E5E0-98C8-E8B7C7C96852";
	setAttr ".cf" 0.017453292519943295;
createNode script -n "uiConfigurationScriptNode";
	rename -uid "20D48E4B-4CA9-F377-F40A-23957F7FF111";
	setAttr ".b" -type "string" (
		"// Maya Mel UI Configuration File.\n//\n//  This script is machine generated.  Edit at your own risk.\n//\n//\n\nglobal string $gMainPane;\nif (`paneLayout -exists $gMainPane`) {\n\n\tglobal int $gUseScenePanelConfig;\n\tint    $useSceneConfig = $gUseScenePanelConfig;\n\tint    $nodeEditorPanelVisible = stringArrayContains(\"nodeEditorPanel1\", `getPanel -vis`);\n\tint    $nodeEditorWorkspaceControlOpen = (`workspaceControl -exists nodeEditorPanel1Window` && `workspaceControl -q -visible nodeEditorPanel1Window`);\n\tint    $menusOkayInPanels = `optionVar -q allowMenusInPanels`;\n\tint    $nVisPanes = `paneLayout -q -nvp $gMainPane`;\n\tint    $nPanes = 0;\n\tstring $editorName;\n\tstring $panelName;\n\tstring $itemFilterName;\n\tstring $panelConfig;\n\n\t//\n\t//  get current state of the UI\n\t//\n\tsceneUIReplacement -update $gMainPane;\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Top View\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Top View\")) -mbv $menusOkayInPanels  $panelName;\n"
		+ "\t\t$editorName = $panelName;\n        modelEditor -e \n            -camera \"top\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"smoothShaded\" \n            -activeOnly 0\n            -ignorePanZoom 0\n            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -holdOuts 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 0\n            -backfaceCulling 0\n            -xray 0\n            -jointXray 1\n            -activeComponentsXray 0\n            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 2.010204\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n            -textureMaxSize 32768\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n"
		+ "            -depthOfFieldPreview 1\n            -maxConstantTransparency 1\n            -rendererName \"vp2Renderer\" \n            -objectFilterShowInHUD 1\n            -isFiltered 0\n            -colorResolution 256 256 \n            -bumpResolution 512 512 \n            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n            -sortTransparent 1\n            -controllers 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n"
		+ "            -hulls 1\n            -grid 1\n            -imagePlane 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -particleInstancers 1\n            -fluids 1\n            -hairSystems 1\n            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -motionTrails 1\n            -clipGhosts 1\n            -greasePencils 1\n            -shadows 0\n            -captureSequenceNumber -1\n            -width 1\n            -height 1\n            -sceneRenderFilter 0\n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n        modelEditor -e \n            -pluginObjects \"gpuCacheDisplayFilter\" 1 \n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n"
		+ "\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Side View\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Side View\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        modelEditor -e \n            -camera \"side\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"smoothShaded\" \n            -activeOnly 0\n            -ignorePanZoom 0\n            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -holdOuts 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 0\n            -backfaceCulling 0\n            -xray 0\n            -jointXray 1\n            -activeComponentsXray 0\n            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 2.010204\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n"
		+ "            -textureDisplay \"modulate\" \n            -textureMaxSize 32768\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n            -depthOfFieldPreview 1\n            -maxConstantTransparency 1\n            -rendererName \"vp2Renderer\" \n            -objectFilterShowInHUD 1\n            -isFiltered 0\n            -colorResolution 256 256 \n            -bumpResolution 512 512 \n            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n"
		+ "            -sortTransparent 1\n            -controllers 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n            -hulls 1\n            -grid 1\n            -imagePlane 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -particleInstancers 1\n            -fluids 1\n            -hairSystems 1\n            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -motionTrails 1\n            -clipGhosts 1\n            -greasePencils 1\n            -shadows 0\n            -captureSequenceNumber -1\n            -width 1\n            -height 1\n"
		+ "            -sceneRenderFilter 0\n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n        modelEditor -e \n            -pluginObjects \"gpuCacheDisplayFilter\" 1 \n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Front View\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Front View\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        modelEditor -e \n            -camera \"front\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"smoothShaded\" \n            -activeOnly 0\n            -ignorePanZoom 0\n            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -holdOuts 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 0\n            -backfaceCulling 0\n"
		+ "            -xray 0\n            -jointXray 1\n            -activeComponentsXray 0\n            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 2.010204\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n            -textureMaxSize 32768\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n            -depthOfFieldPreview 1\n            -maxConstantTransparency 1\n            -rendererName \"vp2Renderer\" \n            -objectFilterShowInHUD 1\n            -isFiltered 0\n            -colorResolution 256 256 \n            -bumpResolution 512 512 \n            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n"
		+ "            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n            -sortTransparent 1\n            -controllers 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n            -hulls 1\n            -grid 1\n            -imagePlane 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -particleInstancers 1\n            -fluids 1\n            -hairSystems 1\n            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n"
		+ "            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -motionTrails 1\n            -clipGhosts 1\n            -greasePencils 1\n            -shadows 0\n            -captureSequenceNumber -1\n            -width 1\n            -height 1\n            -sceneRenderFilter 0\n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n        modelEditor -e \n            -pluginObjects \"gpuCacheDisplayFilter\" 1 \n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Persp View\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Persp View\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        modelEditor -e \n            -camera \"persp\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"smoothShaded\" \n            -activeOnly 0\n"
		+ "            -ignorePanZoom 0\n            -wireframeOnShaded 1\n            -headsUpDisplay 1\n            -holdOuts 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 1\n            -backfaceCulling 0\n            -xray 0\n            -jointXray 1\n            -activeComponentsXray 0\n            -displayTextures 1\n            -smoothWireframe 0\n            -lineWidth 2.010204\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n            -textureMaxSize 32768\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n            -depthOfFieldPreview 1\n            -maxConstantTransparency 1\n            -rendererName \"vp2Renderer\" \n            -objectFilterShowInHUD 1\n            -isFiltered 0\n            -colorResolution 256 256 \n"
		+ "            -bumpResolution 512 512 \n            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n            -sortTransparent 1\n            -controllers 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n            -hulls 1\n            -grid 1\n            -imagePlane 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -particleInstancers 1\n            -fluids 1\n"
		+ "            -hairSystems 1\n            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -motionTrails 1\n            -clipGhosts 1\n            -greasePencils 1\n            -shadows 0\n            -captureSequenceNumber -1\n            -width 1115\n            -height 682\n            -sceneRenderFilter 0\n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n        modelEditor -e \n            -pluginObjects \"gpuCacheDisplayFilter\" 1 \n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"outlinerPanel\" (localizedPanelLabel(\"ToggledOutliner\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\toutlinerPanel -edit -l (localizedPanelLabel(\"ToggledOutliner\")) -mbv $menusOkayInPanels  $panelName;\n"
		+ "\t\t$editorName = $panelName;\n        outlinerEditor -e \n            -docTag \"isolOutln_fromSeln\" \n            -showShapes 0\n            -showAssignedMaterials 0\n            -showTimeEditor 1\n            -showReferenceNodes 1\n            -showReferenceMembers 1\n            -showAttributes 0\n            -showConnected 0\n            -showAnimCurvesOnly 0\n            -showMuteInfo 0\n            -organizeByLayer 1\n            -organizeByClip 1\n            -showAnimLayerWeight 1\n            -autoExpandLayers 1\n            -autoExpand 0\n            -showDagOnly 0\n            -showAssets 1\n            -showContainedOnly 1\n            -showPublishedAsConnected 0\n            -showParentContainers 0\n            -showContainerContents 1\n            -ignoreDagHierarchy 0\n            -expandConnections 0\n            -showUpstreamCurves 1\n            -showUnitlessCurves 1\n            -showCompounds 1\n            -showLeafs 1\n            -showNumericAttrsOnly 0\n            -highlightActive 1\n            -autoSelectNewObjects 0\n"
		+ "            -doNotSelectNewObjects 0\n            -dropIsParent 1\n            -transmitFilters 0\n            -setFilter \"defaultSetFilter\" \n            -showSetMembers 1\n            -allowMultiSelection 1\n            -alwaysToggleSelect 0\n            -directSelect 0\n            -isSet 0\n            -isSetMember 0\n            -displayMode \"DAG\" \n            -expandObjects 0\n            -setsIgnoreFilters 1\n            -containersIgnoreFilters 0\n            -editAttrName 0\n            -showAttrValues 0\n            -highlightSecondary 0\n            -showUVAttrsOnly 0\n            -showTextureNodesOnly 0\n            -attrAlphaOrder \"default\" \n            -animLayerFilterOptions \"allAffecting\" \n            -sortOrder \"none\" \n            -longNames 0\n            -niceNames 1\n            -selectCommand \"{}\" \n            -showNamespace 1\n            -showPinIcons 0\n            -mapMotionTrails 0\n            -ignoreHiddenAttribute 0\n            -ignoreOutlinerColor 0\n            -renderFilterVisible 0\n            -renderFilterIndex 0\n"
		+ "            -selectionOrder \"chronological\" \n            -expandAttribute 0\n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"outlinerPanel\" (localizedPanelLabel(\"Outliner\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\toutlinerPanel -edit -l (localizedPanelLabel(\"Outliner\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        outlinerEditor -e \n            -showShapes 0\n            -showAssignedMaterials 0\n            -showTimeEditor 1\n            -showReferenceNodes 0\n            -showReferenceMembers 0\n            -showAttributes 0\n            -showConnected 0\n            -showAnimCurvesOnly 0\n            -showMuteInfo 0\n            -organizeByLayer 1\n            -organizeByClip 1\n            -showAnimLayerWeight 1\n            -autoExpandLayers 1\n            -autoExpand 0\n            -showDagOnly 1\n            -showAssets 1\n            -showContainedOnly 1\n            -showPublishedAsConnected 0\n"
		+ "            -showParentContainers 0\n            -showContainerContents 1\n            -ignoreDagHierarchy 0\n            -expandConnections 0\n            -showUpstreamCurves 1\n            -showUnitlessCurves 1\n            -showCompounds 1\n            -showLeafs 1\n            -showNumericAttrsOnly 0\n            -highlightActive 1\n            -autoSelectNewObjects 0\n            -doNotSelectNewObjects 0\n            -dropIsParent 1\n            -transmitFilters 0\n            -setFilter \"defaultSetFilter\" \n            -showSetMembers 1\n            -allowMultiSelection 1\n            -alwaysToggleSelect 0\n            -directSelect 0\n            -displayMode \"DAG\" \n            -expandObjects 0\n            -setsIgnoreFilters 1\n            -containersIgnoreFilters 0\n            -editAttrName 0\n            -showAttrValues 0\n            -highlightSecondary 0\n            -showUVAttrsOnly 0\n            -showTextureNodesOnly 0\n            -attrAlphaOrder \"default\" \n            -animLayerFilterOptions \"allAffecting\" \n            -sortOrder \"none\" \n"
		+ "            -longNames 0\n            -niceNames 1\n            -showNamespace 1\n            -showPinIcons 0\n            -mapMotionTrails 0\n            -ignoreHiddenAttribute 0\n            -ignoreOutlinerColor 0\n            -renderFilterVisible 0\n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"graphEditor\" (localizedPanelLabel(\"Graph Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Graph Editor\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"OutlineEd\");\n            outlinerEditor -e \n                -showShapes 1\n                -showAssignedMaterials 0\n                -showTimeEditor 1\n                -showReferenceNodes 0\n                -showReferenceMembers 0\n                -showAttributes 1\n                -showConnected 1\n                -showAnimCurvesOnly 1\n                -showMuteInfo 0\n                -organizeByLayer 1\n"
		+ "                -organizeByClip 1\n                -showAnimLayerWeight 1\n                -autoExpandLayers 1\n                -autoExpand 1\n                -showDagOnly 0\n                -showAssets 1\n                -showContainedOnly 0\n                -showPublishedAsConnected 0\n                -showParentContainers 0\n                -showContainerContents 0\n                -ignoreDagHierarchy 0\n                -expandConnections 1\n                -showUpstreamCurves 1\n                -showUnitlessCurves 1\n                -showCompounds 0\n                -showLeafs 1\n                -showNumericAttrsOnly 1\n                -highlightActive 0\n                -autoSelectNewObjects 1\n                -doNotSelectNewObjects 0\n                -dropIsParent 1\n                -transmitFilters 1\n                -setFilter \"0\" \n                -showSetMembers 0\n                -allowMultiSelection 1\n                -alwaysToggleSelect 0\n                -directSelect 0\n                -displayMode \"DAG\" \n                -expandObjects 0\n"
		+ "                -setsIgnoreFilters 1\n                -containersIgnoreFilters 0\n                -editAttrName 0\n                -showAttrValues 0\n                -highlightSecondary 0\n                -showUVAttrsOnly 0\n                -showTextureNodesOnly 0\n                -attrAlphaOrder \"default\" \n                -animLayerFilterOptions \"allAffecting\" \n                -sortOrder \"none\" \n                -longNames 0\n                -niceNames 1\n                -showNamespace 1\n                -showPinIcons 1\n                -mapMotionTrails 1\n                -ignoreHiddenAttribute 0\n                -ignoreOutlinerColor 0\n                -renderFilterVisible 0\n                $editorName;\n\n\t\t\t$editorName = ($panelName+\"GraphEd\");\n            animCurveEditor -e \n                -displayValues 0\n                -snapTime \"integer\" \n                -snapValue \"none\" \n                -showPlayRangeShades \"on\" \n                -lockPlayRangeShades \"off\" \n                -smoothness \"fine\" \n                -resultSamples 1.25\n"
		+ "                -resultScreenSamples 0\n                -resultUpdate \"delayed\" \n                -showUpstreamCurves 1\n                -keyMinScale 1\n                -stackedCurvesMin -1\n                -stackedCurvesMax 1\n                -stackedCurvesSpace 0.2\n                -preSelectionHighlight 0\n                -constrainDrag 0\n                -valueLinesToggle 0\n                -outliner \"graphEditor1OutlineEd\" \n                -highlightAffectedCurves 0\n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"dopeSheetPanel\" (localizedPanelLabel(\"Dope Sheet\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Dope Sheet\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"OutlineEd\");\n            outlinerEditor -e \n                -showShapes 1\n                -showAssignedMaterials 0\n                -showTimeEditor 1\n                -showReferenceNodes 0\n"
		+ "                -showReferenceMembers 0\n                -showAttributes 1\n                -showConnected 1\n                -showAnimCurvesOnly 1\n                -showMuteInfo 0\n                -organizeByLayer 1\n                -organizeByClip 1\n                -showAnimLayerWeight 1\n                -autoExpandLayers 1\n                -autoExpand 0\n                -showDagOnly 0\n                -showAssets 1\n                -showContainedOnly 0\n                -showPublishedAsConnected 0\n                -showParentContainers 0\n                -showContainerContents 0\n                -ignoreDagHierarchy 0\n                -expandConnections 1\n                -showUpstreamCurves 1\n                -showUnitlessCurves 0\n                -showCompounds 1\n                -showLeafs 1\n                -showNumericAttrsOnly 1\n                -highlightActive 0\n                -autoSelectNewObjects 0\n                -doNotSelectNewObjects 1\n                -dropIsParent 1\n                -transmitFilters 0\n                -setFilter \"0\" \n"
		+ "                -showSetMembers 0\n                -allowMultiSelection 1\n                -alwaysToggleSelect 0\n                -directSelect 0\n                -displayMode \"DAG\" \n                -expandObjects 0\n                -setsIgnoreFilters 1\n                -containersIgnoreFilters 0\n                -editAttrName 0\n                -showAttrValues 0\n                -highlightSecondary 0\n                -showUVAttrsOnly 0\n                -showTextureNodesOnly 0\n                -attrAlphaOrder \"default\" \n                -animLayerFilterOptions \"allAffecting\" \n                -sortOrder \"none\" \n                -longNames 0\n                -niceNames 1\n                -showNamespace 1\n                -showPinIcons 0\n                -mapMotionTrails 1\n                -ignoreHiddenAttribute 0\n                -ignoreOutlinerColor 0\n                -renderFilterVisible 0\n                $editorName;\n\n\t\t\t$editorName = ($panelName+\"DopeSheetEd\");\n            dopeSheetEditor -e \n                -displayValues 0\n                -snapTime \"integer\" \n"
		+ "                -snapValue \"none\" \n                -outliner \"dopeSheetPanel1OutlineEd\" \n                -showSummary 1\n                -showScene 0\n                -hierarchyBelow 0\n                -showTicks 1\n                -selectionWindow 0 0 0 0 \n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"timeEditorPanel\" (localizedPanelLabel(\"Time Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Time Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"clipEditorPanel\" (localizedPanelLabel(\"Trax Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Trax Editor\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = clipEditorNameFromPanel($panelName);\n"
		+ "            clipEditor -e \n                -displayValues 0\n                -snapTime \"none\" \n                -snapValue \"none\" \n                -initialized 0\n                -manageSequencer 0 \n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"sequenceEditorPanel\" (localizedPanelLabel(\"Camera Sequencer\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Camera Sequencer\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = sequenceEditorNameFromPanel($panelName);\n            clipEditor -e \n                -displayValues 0\n                -snapTime \"none\" \n                -snapValue \"none\" \n                -initialized 0\n                -manageSequencer 1 \n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"hyperGraphPanel\" (localizedPanelLabel(\"Hypergraph Hierarchy\")) `;\n"
		+ "\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Hypergraph Hierarchy\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"HyperGraphEd\");\n            hyperGraph -e \n                -graphLayoutStyle \"hierarchicalLayout\" \n                -orientation \"horiz\" \n                -mergeConnections 0\n                -zoom 1\n                -animateTransition 0\n                -showRelationships 1\n                -showShapes 0\n                -showDeformers 0\n                -showExpressions 0\n                -showConstraints 0\n                -showConnectionFromSelected 0\n                -showConnectionToSelected 0\n                -showConstraintLabels 0\n                -showUnderworld 0\n                -showInvisible 0\n                -transitionFrames 1\n                -opaqueContainers 0\n                -freeform 0\n                -imagePosition 0 0 \n                -imageScale 1\n                -imageEnabled 0\n                -graphType \"DAG\" \n"
		+ "                -heatMapDisplay 0\n                -updateSelection 1\n                -updateNodeAdded 1\n                -useDrawOverrideColor 0\n                -limitGraphTraversal -1\n                -range 0 0 \n                -iconSize \"smallIcons\" \n                -showCachedConnections 0\n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"hyperShadePanel\" (localizedPanelLabel(\"Hypershade\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Hypershade\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"visorPanel\" (localizedPanelLabel(\"Visor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Visor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n"
		+ "\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"nodeEditorPanel\" (localizedPanelLabel(\"Node Editor\")) `;\n\tif ($nodeEditorPanelVisible || $nodeEditorWorkspaceControlOpen) {\n\t\tif (\"\" == $panelName) {\n\t\t\tif ($useSceneConfig) {\n\t\t\t\t$panelName = `scriptedPanel -unParent  -type \"nodeEditorPanel\" -l (localizedPanelLabel(\"Node Editor\")) -mbv $menusOkayInPanels `;\n\n\t\t\t$editorName = ($panelName+\"NodeEditorEd\");\n            nodeEditor -e \n                -allAttributes 0\n                -allNodes 0\n                -autoSizeNodes 1\n                -consistentNameSize 1\n                -createNodeCommand \"nodeEdCreateNodeCommand\" \n                -connectNodeOnCreation 0\n                -connectOnDrop 0\n                -copyConnectionsOnPaste 0\n                -connectionStyle \"bezier\" \n                -connectionMinSegment 0.03\n                -connectionOffset 0.03\n                -connectionRoundness 0.8\n                -connectionTension -100\n                -defaultPinnedState 0\n"
		+ "                -additiveGraphingMode 0\n                -settingsChangedCallback \"nodeEdSyncControls\" \n                -traversalDepthLimit -1\n                -keyPressCommand \"nodeEdKeyPressCommand\" \n                -nodeTitleMode \"name\" \n                -gridSnap 0\n                -gridVisibility 1\n                -crosshairOnEdgeDragging 0\n                -popupMenuScript \"nodeEdBuildPanelMenus\" \n                -showNamespace 1\n                -showShapes 1\n                -showSGShapes 0\n                -showTransforms 1\n                -useAssets 1\n                -syncedSelection 1\n                -extendToShapes 1\n                -editorMode \"default\" \n                -hasWatchpoint 0\n                $editorName;\n\t\t\t}\n\t\t} else {\n\t\t\t$label = `panel -q -label $panelName`;\n\t\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Node Editor\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"NodeEditorEd\");\n            nodeEditor -e \n                -allAttributes 0\n                -allNodes 0\n                -autoSizeNodes 1\n"
		+ "                -consistentNameSize 1\n                -createNodeCommand \"nodeEdCreateNodeCommand\" \n                -connectNodeOnCreation 0\n                -connectOnDrop 0\n                -copyConnectionsOnPaste 0\n                -connectionStyle \"bezier\" \n                -connectionMinSegment 0.03\n                -connectionOffset 0.03\n                -connectionRoundness 0.8\n                -connectionTension -100\n                -defaultPinnedState 0\n                -additiveGraphingMode 0\n                -settingsChangedCallback \"nodeEdSyncControls\" \n                -traversalDepthLimit -1\n                -keyPressCommand \"nodeEdKeyPressCommand\" \n                -nodeTitleMode \"name\" \n                -gridSnap 0\n                -gridVisibility 1\n                -crosshairOnEdgeDragging 0\n                -popupMenuScript \"nodeEdBuildPanelMenus\" \n                -showNamespace 1\n                -showShapes 1\n                -showSGShapes 0\n                -showTransforms 1\n                -useAssets 1\n                -syncedSelection 1\n"
		+ "                -extendToShapes 1\n                -editorMode \"default\" \n                -hasWatchpoint 0\n                $editorName;\n\t\t\tif (!$useSceneConfig) {\n\t\t\t\tpanel -e -l $label $panelName;\n\t\t\t}\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"createNodePanel\" (localizedPanelLabel(\"Create Node\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Create Node\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"polyTexturePlacementPanel\" (localizedPanelLabel(\"UV Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"UV Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"renderWindowPanel\" (localizedPanelLabel(\"Render View\")) `;\n"
		+ "\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Render View\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"shapePanel\" (localizedPanelLabel(\"Shape Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tshapePanel -edit -l (localizedPanelLabel(\"Shape Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"posePanel\" (localizedPanelLabel(\"Pose Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tposePanel -edit -l (localizedPanelLabel(\"Pose Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"dynRelEdPanel\" (localizedPanelLabel(\"Dynamic Relationships\")) `;\n\tif (\"\" != $panelName) {\n"
		+ "\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Dynamic Relationships\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"relationshipPanel\" (localizedPanelLabel(\"Relationship Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Relationship Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"referenceEditorPanel\" (localizedPanelLabel(\"Reference Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Reference Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"componentEditorPanel\" (localizedPanelLabel(\"Component Editor\")) `;\n"
		+ "\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Component Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"dynPaintScriptedPanelType\" (localizedPanelLabel(\"Paint Effects\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Paint Effects\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"scriptEditorPanel\" (localizedPanelLabel(\"Script Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Script Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"profilerPanel\" (localizedPanelLabel(\"Profiler Tool\")) `;\n"
		+ "\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Profiler Tool\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"contentBrowserPanel\" (localizedPanelLabel(\"Content Browser\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Content Browser\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"Stereo\" (localizedPanelLabel(\"Stereo\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Stereo\")) -mbv $menusOkayInPanels  $panelName;\n{ string $editorName = ($panelName+\"Editor\");\n            stereoCameraView -e \n                -camera \"persp\" \n                -useInteractiveMode 0\n                -displayLights \"default\" \n"
		+ "                -displayAppearance \"wireframe\" \n                -activeOnly 0\n                -ignorePanZoom 0\n                -wireframeOnShaded 0\n                -headsUpDisplay 1\n                -holdOuts 1\n                -selectionHiliteDisplay 1\n                -useDefaultMaterial 0\n                -bufferMode \"double\" \n                -twoSidedLighting 1\n                -backfaceCulling 0\n                -xray 0\n                -jointXray 0\n                -activeComponentsXray 0\n                -displayTextures 0\n                -smoothWireframe 0\n                -lineWidth 2.010204\n                -textureAnisotropic 0\n                -textureHilight 1\n                -textureSampling 2\n                -textureDisplay \"modulate\" \n                -textureMaxSize 32768\n                -fogging 0\n                -fogSource \"fragment\" \n                -fogMode \"linear\" \n                -fogStart 0\n                -fogEnd 100\n                -fogDensity 0.1\n                -fogColor 0.5 0.5 0.5 1 \n                -depthOfFieldPreview 1\n"
		+ "                -maxConstantTransparency 1\n                -objectFilterShowInHUD 1\n                -isFiltered 0\n                -colorResolution 4 4 \n                -bumpResolution 4 4 \n                -textureCompression 0\n                -transparencyAlgorithm \"frontAndBackCull\" \n                -transpInShadows 0\n                -cullingOverride \"none\" \n                -lowQualityLighting 0\n                -maximumNumHardwareLights 0\n                -occlusionCulling 0\n                -shadingModel 0\n                -useBaseRenderer 0\n                -useReducedRenderer 0\n                -smallObjectCulling 0\n                -smallObjectThreshold -1 \n                -interactiveDisableShadows 0\n                -interactiveBackFaceCull 0\n                -sortTransparent 1\n                -controllers 1\n                -nurbsCurves 1\n                -nurbsSurfaces 1\n                -polymeshes 1\n                -subdivSurfaces 1\n                -planes 1\n                -lights 1\n                -cameras 1\n"
		+ "                -controlVertices 1\n                -hulls 1\n                -grid 1\n                -imagePlane 1\n                -joints 1\n                -ikHandles 1\n                -deformers 1\n                -dynamics 1\n                -particleInstancers 1\n                -fluids 1\n                -hairSystems 1\n                -follicles 1\n                -nCloths 1\n                -nParticles 1\n                -nRigids 1\n                -dynamicConstraints 1\n                -locators 1\n                -manipulators 1\n                -pluginShapes 1\n                -dimensions 1\n                -handles 1\n                -pivots 1\n                -textures 1\n                -strokes 1\n                -motionTrails 1\n                -clipGhosts 1\n                -greasePencils 1\n                -shadows 0\n                -captureSequenceNumber -1\n                -width 0\n                -height 0\n                -sceneRenderFilter 0\n                -displayMode \"centerEye\" \n                -viewColor 0 0 0 1 \n"
		+ "                -useCustomBackground 1\n                $editorName;\n            stereoCameraView -e -viewSelected 0 $editorName;\n            stereoCameraView -e \n                -pluginObjects \"gpuCacheDisplayFilter\" 1 \n                $editorName; };\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\tif ($useSceneConfig) {\n        string $configName = `getPanel -cwl (localizedPanelLabel(\"Current Layout\"))`;\n        if (\"\" != $configName) {\n\t\t\tpanelConfiguration -edit -label (localizedPanelLabel(\"Current Layout\")) \n\t\t\t\t-userCreated false\n\t\t\t\t-defaultImage \"vacantCell.xP:/\"\n\t\t\t\t-image \"\"\n\t\t\t\t-sc false\n\t\t\t\t-configString \"global string $gMainPane; paneLayout -e -cn \\\"single\\\" -ps 1 100 100 $gMainPane;\"\n\t\t\t\t-removeAllPanels\n\t\t\t\t-ap false\n\t\t\t\t\t(localizedPanelLabel(\"Persp View\")) \n\t\t\t\t\t\"modelPanel\"\n"
		+ "\t\t\t\t\t\"$panelName = `modelPanel -unParent -l (localizedPanelLabel(\\\"Persp View\\\")) -mbv $menusOkayInPanels `;\\n$editorName = $panelName;\\nmodelEditor -e \\n    -cam `findStartUpCamera persp` \\n    -useInteractiveMode 0\\n    -displayLights \\\"default\\\" \\n    -displayAppearance \\\"smoothShaded\\\" \\n    -activeOnly 0\\n    -ignorePanZoom 0\\n    -wireframeOnShaded 1\\n    -headsUpDisplay 1\\n    -holdOuts 1\\n    -selectionHiliteDisplay 1\\n    -useDefaultMaterial 0\\n    -bufferMode \\\"double\\\" \\n    -twoSidedLighting 1\\n    -backfaceCulling 0\\n    -xray 0\\n    -jointXray 1\\n    -activeComponentsXray 0\\n    -displayTextures 1\\n    -smoothWireframe 0\\n    -lineWidth 2.010204\\n    -textureAnisotropic 0\\n    -textureHilight 1\\n    -textureSampling 2\\n    -textureDisplay \\\"modulate\\\" \\n    -textureMaxSize 32768\\n    -fogging 0\\n    -fogSource \\\"fragment\\\" \\n    -fogMode \\\"linear\\\" \\n    -fogStart 0\\n    -fogEnd 100\\n    -fogDensity 0.1\\n    -fogColor 0.5 0.5 0.5 1 \\n    -depthOfFieldPreview 1\\n    -maxConstantTransparency 1\\n    -rendererName \\\"vp2Renderer\\\" \\n    -objectFilterShowInHUD 1\\n    -isFiltered 0\\n    -colorResolution 256 256 \\n    -bumpResolution 512 512 \\n    -textureCompression 0\\n    -transparencyAlgorithm \\\"frontAndBackCull\\\" \\n    -transpInShadows 0\\n    -cullingOverride \\\"none\\\" \\n    -lowQualityLighting 0\\n    -maximumNumHardwareLights 1\\n    -occlusionCulling 0\\n    -shadingModel 0\\n    -useBaseRenderer 0\\n    -useReducedRenderer 0\\n    -smallObjectCulling 0\\n    -smallObjectThreshold -1 \\n    -interactiveDisableShadows 0\\n    -interactiveBackFaceCull 0\\n    -sortTransparent 1\\n    -controllers 1\\n    -nurbsCurves 1\\n    -nurbsSurfaces 1\\n    -polymeshes 1\\n    -subdivSurfaces 1\\n    -planes 1\\n    -lights 1\\n    -cameras 1\\n    -controlVertices 1\\n    -hulls 1\\n    -grid 1\\n    -imagePlane 1\\n    -joints 1\\n    -ikHandles 1\\n    -deformers 1\\n    -dynamics 1\\n    -particleInstancers 1\\n    -fluids 1\\n    -hairSystems 1\\n    -follicles 1\\n    -nCloths 1\\n    -nParticles 1\\n    -nRigids 1\\n    -dynamicConstraints 1\\n    -locators 1\\n    -manipulators 1\\n    -pluginShapes 1\\n    -dimensions 1\\n    -handles 1\\n    -pivots 1\\n    -textures 1\\n    -strokes 1\\n    -motionTrails 1\\n    -clipGhosts 1\\n    -greasePencils 1\\n    -shadows 0\\n    -captureSequenceNumber -1\\n    -width 1115\\n    -height 682\\n    -sceneRenderFilter 0\\n    $editorName;\\nmodelEditor -e -viewSelected 0 $editorName;\\nmodelEditor -e \\n    -pluginObjects \\\"gpuCacheDisplayFilter\\\" 1 \\n    $editorName\"\n"
		+ "\t\t\t\t\t\"modelPanel -edit -l (localizedPanelLabel(\\\"Persp View\\\")) -mbv $menusOkayInPanels  $panelName;\\n$editorName = $panelName;\\nmodelEditor -e \\n    -cam `findStartUpCamera persp` \\n    -useInteractiveMode 0\\n    -displayLights \\\"default\\\" \\n    -displayAppearance \\\"smoothShaded\\\" \\n    -activeOnly 0\\n    -ignorePanZoom 0\\n    -wireframeOnShaded 1\\n    -headsUpDisplay 1\\n    -holdOuts 1\\n    -selectionHiliteDisplay 1\\n    -useDefaultMaterial 0\\n    -bufferMode \\\"double\\\" \\n    -twoSidedLighting 1\\n    -backfaceCulling 0\\n    -xray 0\\n    -jointXray 1\\n    -activeComponentsXray 0\\n    -displayTextures 1\\n    -smoothWireframe 0\\n    -lineWidth 2.010204\\n    -textureAnisotropic 0\\n    -textureHilight 1\\n    -textureSampling 2\\n    -textureDisplay \\\"modulate\\\" \\n    -textureMaxSize 32768\\n    -fogging 0\\n    -fogSource \\\"fragment\\\" \\n    -fogMode \\\"linear\\\" \\n    -fogStart 0\\n    -fogEnd 100\\n    -fogDensity 0.1\\n    -fogColor 0.5 0.5 0.5 1 \\n    -depthOfFieldPreview 1\\n    -maxConstantTransparency 1\\n    -rendererName \\\"vp2Renderer\\\" \\n    -objectFilterShowInHUD 1\\n    -isFiltered 0\\n    -colorResolution 256 256 \\n    -bumpResolution 512 512 \\n    -textureCompression 0\\n    -transparencyAlgorithm \\\"frontAndBackCull\\\" \\n    -transpInShadows 0\\n    -cullingOverride \\\"none\\\" \\n    -lowQualityLighting 0\\n    -maximumNumHardwareLights 1\\n    -occlusionCulling 0\\n    -shadingModel 0\\n    -useBaseRenderer 0\\n    -useReducedRenderer 0\\n    -smallObjectCulling 0\\n    -smallObjectThreshold -1 \\n    -interactiveDisableShadows 0\\n    -interactiveBackFaceCull 0\\n    -sortTransparent 1\\n    -controllers 1\\n    -nurbsCurves 1\\n    -nurbsSurfaces 1\\n    -polymeshes 1\\n    -subdivSurfaces 1\\n    -planes 1\\n    -lights 1\\n    -cameras 1\\n    -controlVertices 1\\n    -hulls 1\\n    -grid 1\\n    -imagePlane 1\\n    -joints 1\\n    -ikHandles 1\\n    -deformers 1\\n    -dynamics 1\\n    -particleInstancers 1\\n    -fluids 1\\n    -hairSystems 1\\n    -follicles 1\\n    -nCloths 1\\n    -nParticles 1\\n    -nRigids 1\\n    -dynamicConstraints 1\\n    -locators 1\\n    -manipulators 1\\n    -pluginShapes 1\\n    -dimensions 1\\n    -handles 1\\n    -pivots 1\\n    -textures 1\\n    -strokes 1\\n    -motionTrails 1\\n    -clipGhosts 1\\n    -greasePencils 1\\n    -shadows 0\\n    -captureSequenceNumber -1\\n    -width 1115\\n    -height 682\\n    -sceneRenderFilter 0\\n    $editorName;\\nmodelEditor -e -viewSelected 0 $editorName;\\nmodelEditor -e \\n    -pluginObjects \\\"gpuCacheDisplayFilter\\\" 1 \\n    $editorName\"\n"
		+ "\t\t\t\t$configName;\n\n            setNamedPanelLayout (localizedPanelLabel(\"Current Layout\"));\n        }\n\n        panelHistory -e -clear mainPanelHistory;\n        sceneUIReplacement -clear;\n\t}\n\n\ngrid -spacing 20 -size 2000 -divisions 1 -displayAxes yes -displayGridLines yes -displayDivisionLines yes -displayPerspectiveLabels no -displayOrthographicLabels yes -displayAxesBold yes -perspectiveLabelPosition axis -orthographicLabelPosition edge;\nviewManip -drawCompass 0 -compassAngle 0 -frontParameters \"\" -homeParameters \"\" -selectionLockParameters \"\";\n}\n");
	setAttr ".st" 3;
createNode script -n "sceneConfigurationScriptNode";
	rename -uid "A3F2E9C4-4989-6F9E-F276-6F9C9EBD1330";
	setAttr ".b" -type "string" "playbackOptions -min 0 -max 150 -ast 0 -aet 250 ";
	setAttr ".st" 6;
createNode nodeGraphEditorInfo -n "hyperShadePrimaryNodeEditorSavedTabsInfo4";
	rename -uid "B802F317-4E67-5CB4-27F6-DBB34E43DD91";
	setAttr ".tgi[0].tn" -type "string" "�ޱ���_1";
	setAttr ".tgi[0].vl" -type "double2" -891.66663123501826 -861.95778021648403 ;
	setAttr ".tgi[0].vh" -type "double2" 773.80949306109744 217.910186761017 ;
	setAttr -s 3 ".tgi[0].ni";
	setAttr ".tgi[0].ni[0].x" 1.4285714626312256;
	setAttr ".tgi[0].ni[0].y" -670;
	setAttr ".tgi[0].ni[0].nvs" 1923;
	setAttr ".tgi[0].ni[1].x" -151.42857360839844;
	setAttr ".tgi[0].ni[1].y" -224.28572082519531;
	setAttr ".tgi[0].ni[1].nvs" 1923;
	setAttr ".tgi[0].ni[2].x" 1.4285714626312256;
	setAttr ".tgi[0].ni[2].y" 218.57142639160156;
	setAttr ".tgi[0].ni[2].nvs" 1922;
createNode condition -n "con_l_handIk_00";
	rename -uid "1D272333-4B67-AA4F-5B60-2E9B5386C8BF";
	setAttr ".ct" -type "float3" 1 1 1 ;
	setAttr ".cf" -type "float3" 0 0 0 ;
createNode condition -n "con_l_handIk_01";
	rename -uid "5A912939-4369-C87E-B8B7-638B7C80B3C1";
	setAttr ".st" 1;
	setAttr ".ct" -type "float3" 1 1 1 ;
	setAttr ".cf" -type "float3" 0 0 0 ;
createNode condition -n "con_l_handIk_02";
	rename -uid "3D18EA48-4D0E-3EF4-705E-BDB6652ADB6F";
	setAttr ".st" 2;
	setAttr ".ct" -type "float3" 1 1 1 ;
	setAttr ".cf" -type "float3" 0 0 0 ;
createNode condition -n "con_l_handIk_03";
	rename -uid "DBA4B19C-46C3-612F-7353-D4992FB8DA8D";
	setAttr ".st" 3;
	setAttr ".ct" -type "float3" 1 1 1 ;
	setAttr ".cf" -type "float3" 0 0 0 ;
createNode condition -n "con_l_armPv_00";
	rename -uid "5947123C-4B76-EF79-DEEA-468B9D603573";
	setAttr ".ct" -type "float3" 1 1 1 ;
	setAttr ".cf" -type "float3" 0 0 0 ;
createNode condition -n "con_l_armPv_01";
	rename -uid "807898EC-43C4-C00F-B068-C6A7098A320F";
	setAttr ".st" 1;
	setAttr ".ct" -type "float3" 1 1 1 ;
	setAttr ".cf" -type "float3" 0 0 0 ;
createNode nodeGraphEditorInfo -n "MayaNodeEditorSavedTabsInfo";
	rename -uid "69503D68-48C8-0648-A981-D09614055411";
	setAttr ".tgi[0].tn" -type "string" "�ޱ���_1";
	setAttr ".tgi[0].vl" -type "double2" 10372.203772549838 7458.3330369658061 ;
	setAttr ".tgi[0].vh" -type "double2" 11978.985815484162 8238.0949107427568 ;
	setAttr -s 6 ".tgi[0].ni";
	setAttr ".tgi[0].ni[0].x" 11163.4453125;
	setAttr ".tgi[0].ni[0].y" 7796.21826171875;
	setAttr ".tgi[0].ni[0].nvs" 18304;
	setAttr ".tgi[0].ni[1].x" 10818.9912109375;
	setAttr ".tgi[0].ni[1].y" 8322.60546875;
	setAttr ".tgi[0].ni[1].nvs" 18306;
	setAttr ".tgi[0].ni[2].x" 11218.5712890625;
	setAttr ".tgi[0].ni[2].y" 8181.4287109375;
	setAttr ".tgi[0].ni[2].nvs" 18304;
	setAttr ".tgi[0].ni[3].x" 11165.791015625;
	setAttr ".tgi[0].ni[3].y" 7923.458984375;
	setAttr ".tgi[0].ni[3].nvs" 18304;
	setAttr ".tgi[0].ni[4].x" 11528.5712890625;
	setAttr ".tgi[0].ni[4].y" 8048.5712890625;
	setAttr ".tgi[0].ni[4].nvs" 18304;
	setAttr ".tgi[0].ni[5].x" 11525.7138671875;
	setAttr ".tgi[0].ni[5].y" 8181.4287109375;
	setAttr ".tgi[0].ni[5].nvs" 18304;
select -ne :time1;
	setAttr ".o" 0;
select -ne :hardwareRenderingGlobals;
	setAttr ".otfna" -type "stringArray" 22 "NURBS Curves" "NURBS Surfaces" "Polygons" "Subdiv Surface" "Particles" "Particle Instance" "Fluids" "Strokes" "Image Planes" "UI" "Lights" "Cameras" "Locators" "Joints" "IK Handles" "Deformers" "Motion Trails" "Components" "Hair Systems" "Follicles" "Misc. UI" "Ornaments"  ;
	setAttr ".otfva" -type "Int32Array" 22 0 1 1 1 1 1
		 1 1 1 0 0 0 0 0 0 0 0 0
		 0 0 0 0 ;
	setAttr ".msaa" yes;
	setAttr ".fprt" yes;
select -ne :renderPartition;
	setAttr -s 2 ".st";
select -ne :renderGlobalsList1;
select -ne :defaultShaderList1;
	setAttr -s 5 ".s";
select -ne :postProcessList1;
	setAttr -s 2 ".p";
select -ne :defaultRenderUtilityList1;
	setAttr -s 12 ".u";
select -ne :defaultRenderingList1;
select -ne :initialShadingGroup;
	setAttr ".ro" yes;
select -ne :initialParticleSE;
	setAttr ".ro" yes;
select -ne :defaultRenderGlobals;
	addAttr -ci true -h true -sn "dss" -ln "defaultSurfaceShader" -dt "string";
	setAttr ".dss" -type "string" "lambert1";
select -ne :defaultResolution;
	setAttr ".pa" 1;
select -ne :defaultColorMgtGlobals;
	setAttr ".cfe" yes;
	setAttr ".cfp" -type "string" "<MAYA_RESOURCES>/OCIO-configs/Maya2022-default/config.ocio";
	setAttr ".wsn" -type "string" "ACEScg";
select -ne :hardwareRenderGlobals;
	setAttr ".ctrs" 256;
	setAttr ".btrs" 512;
connectAttr "add_l_armIk.o" "grp_l_armIk.v";
connectAttr "dec_l_forearmIk.ot" "crv_l_armPvCurveShape.cp[0]";
connectAttr "dec_l_armPv.ot" "crv_l_armPvCurveShape.cp[1]";
connectAttr "jnt_l_upperarmIk.s" "jnt_l_forearmIk.is";
connectAttr "jnt_l_forearmIk.s" "jnt_l_handIk.is";
connectAttr "add_l_armFk.o" "driven_l_upperarmFk.v";
connectAttr "ctrl_l_upperarmSub.t" "output_l_upperarmFk.t";
connectAttr "ctrl_l_upperarmSub.r" "output_l_upperarmFk.r";
connectAttr "ctrl_l_upperarmSub.s" "output_l_upperarmFk.s";
connectAttr "ctrl_l_upperarmFk.subCtrlVis" "ctrl_l_upperarmSub.v" -l on;
connectAttr "unitConversion159.o" "offset_l_finThumbB.rz";
relationship "link" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
connectAttr "layerManager.dli[0]" "defaultLayer.id";
connectAttr "renderLayerManager.rlmi[0]" "defaultRenderLayer.rlid";
connectAttr "ctrl_l_armPv.wm" "dec_l_armPv.imat";
connectAttr "ctrl_l_armBlendIkFk.ty" "rem_l_armBlendIkFk.i";
connectAttr "rem_l_armBlendIkFk.ov" "rev_l_armBlendIkFk.ix";
connectAttr "ctrl_l_armBlendIkFk.ikFkVis" "rev_l_armBlendIkFk.iy";
connectAttr "rev_l_armBlendIkFk.oy" "add_l_armIk.i1";
connectAttr "rem_l_armBlendIkFk.ov" "add_l_armIk.i2";
connectAttr "rev_l_armBlendIkFk.ox" "add_l_armFk.i1";
connectAttr "rev_l_armBlendIkFk.oy" "add_l_armFk.i2";
connectAttr "jnt_l_forearmIk.wm" "dec_l_forearmIk.imat";
connectAttr "ctrl_l_finThumbA.fingerBent" "unitConversion159.i";
connectAttr "ctrl_l_finPinkyCarpal.msg" "hyperShadePrimaryNodeEditorSavedTabsInfo4.tgi[0].ni[0].dn"
		;
connectAttr "zero_l_finPinkyCarpal.msg" "hyperShadePrimaryNodeEditorSavedTabsInfo4.tgi[0].ni[1].dn"
		;
connectAttr "ctrl_l_finPinkyCarpalShape.msg" "hyperShadePrimaryNodeEditorSavedTabsInfo4.tgi[0].ni[2].dn"
		;
connectAttr "ctrl_l_handIk.space" "con_l_handIk_00.ft";
connectAttr "ctrl_l_handIk.space" "con_l_handIk_01.ft";
connectAttr "ctrl_l_handIk.space" "con_l_handIk_02.ft";
connectAttr "ctrl_l_handIk.space" "con_l_handIk_03.ft";
connectAttr "ctrl_l_armPv.space" "con_l_armPv_00.ft";
connectAttr "ctrl_l_armPv.space" "con_l_armPv_01.ft";
connectAttr "con_l_armPv_01.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[0].dn";
connectAttr "ctrl_l_armPv.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[1].dn";
connectAttr "dec_l_armPv.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[2].dn";
connectAttr "con_l_armPv_00.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[3].dn";
connectAttr "ctrl_l_armPvShape.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[4].dn"
		;
connectAttr "crv_l_armPvCurveShape.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[5].dn"
		;
connectAttr "dec_l_armPv.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "dec_l_forearmIk.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "rem_l_armBlendIkFk.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "rev_l_armBlendIkFk.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "add_l_armIk.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "add_l_armFk.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "con_l_handIk_00.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "con_l_handIk_01.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "con_l_handIk_02.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "con_l_handIk_03.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "con_l_armPv_00.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "con_l_armPv_01.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "defaultRenderLayer.msg" ":defaultRenderingList1.r" -na;
// End of controls_l_arm.ma
