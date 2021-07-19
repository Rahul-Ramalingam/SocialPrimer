import 'package:bloc/bloc.dart';
import 'package:sidebar_animation/pages/aboutpage.dart';
import 'package:sidebar_animation/pages/locationspage.dart';
import '../pages/homepage.dart';

enum NavigationEvents {
  HomePageClickedEvent,
  MyAccountClickedEvent,
  MyOrdersClickedEvent,
}

abstract class NavigationStates {}

class NavigationBloc extends Bloc<NavigationEvents, NavigationStates> {
  @override
  NavigationStates get initialState => HomePage();

  @override
  Stream<NavigationStates> mapEventToState(NavigationEvents event) async* {
    switch (event) {
      case NavigationEvents.HomePageClickedEvent:
        yield HomePage();
        break;
      case NavigationEvents.MyAccountClickedEvent:
        yield LocationsPage();
        break;
      case NavigationEvents.MyOrdersClickedEvent:
        yield AboutPage();
        break;
    }
  }
}
