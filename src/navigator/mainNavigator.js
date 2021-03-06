import { createAppContainer } from 'react-navigation';
import { createStackNavigator } from 'react-navigation-stack';
import {createDrawerNavigator} from 'react-navigation-drawer';

import SplashScreen from "../features/SplashScreen";
import SideMenu from './sideMenu';
//@BlueprintImportInsertion
import UserProfile207863Navigator from '../features/UserProfile207863/navigator';
import Tutorial207862Navigator from '../features/Tutorial207862/navigator';
import NotificationList207834Navigator from '../features/NotificationList207834/navigator';
import Settings207833Navigator from '../features/Settings207833/navigator';
import Settings207825Navigator from '../features/Settings207825/navigator';
import UserProfile207823Navigator from '../features/UserProfile207823/navigator';

/**
 * new navigators can be imported here
 */

const AppNavigator = {

    //@BlueprintNavigationInsertion
UserProfile207863: { screen: UserProfile207863Navigator },
Tutorial207862: { screen: Tutorial207862Navigator },
NotificationList207834: { screen: NotificationList207834Navigator },
Settings207833: { screen: Settings207833Navigator },
Settings207825: { screen: Settings207825Navigator },
UserProfile207823: { screen: UserProfile207823Navigator },

    /** new navigators can be added here */
    SplashScreen: {
      screen: SplashScreen
    }
};

const DrawerAppNavigator = createDrawerNavigator(
  {
    ...AppNavigator,
  },
  {
    contentComponent: SideMenu
  },
);

const AppContainer = createAppContainer(DrawerAppNavigator);

export default AppContainer;
