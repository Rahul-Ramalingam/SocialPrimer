import 'package:flutter/material.dart';
import '../bloc.navigation_bloc/navigation_bloc.dart';
import 'dart:async';
import 'package:webview_flutter/webview_flutter.dart';


class LocationsPage extends StatefulWidget with NavigationStates {
  @override
  _WebViewExampleState createState() => _WebViewExampleState();
}

class _WebViewExampleState extends State<LocationsPage> {
  final Completer<WebViewController> _controller =
      Completer<WebViewController>();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
     
      body: Builder(builder: (BuildContext context) {
        return Container(
          child:Padding(
            padding: EdgeInsets.fromLTRB(0, 10, 0, 0), 
            child: WebView(
            initialUrl: 'https://locationappp.herokuapp.com/home/',
            javascriptMode: JavascriptMode.unrestricted,
            onWebViewCreated: (WebViewController webViewController) {
              _controller.complete(webViewController);
            },
          ),
        ));
      }),
    );
  }
}
