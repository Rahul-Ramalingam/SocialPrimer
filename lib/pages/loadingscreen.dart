import 'dart:async';

import 'package:flutter/material.dart';
import 'package:flutter/rendering.dart';
import 'package:flutter_spinkit/flutter_spinkit.dart';
import 'package:sidebar_animation/data/data.dart';
import 'package:sidebar_animation/sidebar/sidebar_layout.dart';

class LoadingScreen extends StatefulWidget{
  @override
  _LoadingScreenState createState() => _LoadingScreenState();
}


class _LoadingScreenState extends State<LoadingScreen>{
  @override
  void initState(){
    super.initState();
    _mockCheckForSession().then(
        (status) {
          if (status) {
            _navigateToHome();
          } else {
            _navigateToHome();
          }
        }
    );
  }


  Future<bool> _mockCheckForSession() async {
    await Future.delayed(Duration(milliseconds: 5000), () {});

    return true;
  }

  void _navigateToHome(){
    Navigator.of(context).pushReplacement(
      MaterialPageRoute(
        builder: (BuildContext context) => SideBarLayout()
      )
    );
  }

  
  @override
  Widget build(BuildContext context){
    return Scaffold(
      body:Stack(
        fit:StackFit.expand,
        children: <Widget>[
        Container(
          decoration: BoxDecoration(
            color: new Color(0xff622F74),
            gradient: LinearGradient(
              colors: [new Color(0xff29dfb7),new Color(0xff3ec7fd)],
              begin: Alignment.topCenter,
              end: Alignment.bottomCenter
              ) 
            )
        ),
        Column(
          mainAxisAlignment:MainAxisAlignment.spaceEvenly,
          children: <Widget>[
            CircleAvatar(
            radius: (60),
            backgroundColor: Colors.transparent,
            child: ClipRRect(
              borderRadius:BorderRadius.circular(180),
              child: Image.asset(getSlides()[10].getImageAssetPath()),
            )
        ),
        Text("Social Primer",
              textAlign: TextAlign.center,
              style: TextStyle(color:Colors.white,fontSize:20, fontWeight:FontWeight.w500),)
           
          ],
          ),

        Padding(
          padding: EdgeInsets.fromLTRB(0, 500, 0, 0),
          child:SpinKitFadingCube(
            color: Colors.white,
            size: 30.0
          )
        )
        ],
      )
    );
  }
}