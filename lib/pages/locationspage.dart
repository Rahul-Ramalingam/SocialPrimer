import 'package:flutter/material.dart';
import 'package:sidebar_animation/pages/camstream.dart';

import '../bloc.navigation_bloc/navigation_bloc.dart';

class HomePage extends StatelessWidget with NavigationStates {
  @override
Widget build(BuildContext context) {
        return ListView(
          //mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            SizedBox(height: 40.0,),
            Container(
      padding: EdgeInsets.all(20.0),
      decoration: BoxDecoration(
            color:Colors.white,
            borderRadius: BorderRadius.circular(20.0),
            boxShadow: [
              BoxShadow(
                color: Colors.grey,
                blurRadius:10.0,
                spreadRadius: 1.0,
                offset: Offset(4.0, 4.0),
              )
            ]
      ),
      child:Column(
            children: <Widget>[
              Padding(
                padding: EdgeInsets.symmetric(vertical: 20.0, horizontal: 8.0),
                child: Text(
                  "Garden View",
                  style: TextStyle(
                    color: Colors.blueGrey,
                    fontSize: 25.0,
                    fontWeight: FontWeight.bold,
                  ),
                ),
              ),
                RaisedButton(
                  child: Text("Camera 3"),
                  onPressed: (){
                      Navigator.push(context, MaterialPageRoute(builder: (context)=> VideoPage1()));
                    }),
                    ]
                    ),
                    ),
                    ]
                    );
                    }}
