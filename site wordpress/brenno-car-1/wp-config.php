<?php
define( 'WP_CACHE', true );
/**
 * The base configuration for WordPress
 *
 * The wp-config.php creation script uses this file during the installation.
 * You don't have to use the web site, you can copy this file to "wp-config.php"
 * and fill in the values.
 *
 * This file contains the following configurations:
 *
 * * Database settings
 * * Secret keys
 * * Database table prefix
 * * Localized language
 * * ABSPATH
 *
 * @link https://wordpress.org/support/article/editing-wp-config-php/
 *
 * @package WordPress
 */

// ** Database settings - You can get this info from your web host ** //
/** The name of the database for WordPress */
define( 'DB_NAME', 'u928010470_g6LXf' );

/** Database username */
define( 'DB_USER', 'u928010470_8KXg2' );

/** Database password */
define( 'DB_PASSWORD', 'LOokYroBmM' );

/** Database hostname */
define( 'DB_HOST', '127.0.0.1' );

/** Database charset to use in creating database tables. */
define( 'DB_CHARSET', 'utf8' );

/** The database collate type. Don't change this if in doubt. */
define( 'DB_COLLATE', '' );

/**#@+
 * Authentication unique keys and salts.
 *
 * Change these to different unique phrases! You can generate these using
 * the {@link https://api.wordpress.org/secret-key/1.1/salt/ WordPress.org secret-key service}.
 *
 * You can change these at any point in time to invalidate all existing cookies.
 * This will force all users to have to log in again.
 *
 * @since 2.6.0
 */
define( 'AUTH_KEY',          'DuUKMFD>0:ZW<!|P7*}.X~Hk}nd-d:fx5Lr6$Gn2o|F:p0x2[(|q41{Gr6][3F{%' );
define( 'SECURE_AUTH_KEY',   'o0jiv@b$+4!9^YhCtoc]VF`fapc`ZxnF!DTnV`W+gp=ZF%@=`#4wzzq1+X#QP&%w' );
define( 'LOGGED_IN_KEY',     '8B45RXHRm`x!02HgE2|^+^#vQbxGaZ>,l/2BG{<lhr?|=&/MaGA)(!gwZ6jg6BBB' );
define( 'NONCE_KEY',         '|k&{.XI}:-@$LtmT2%8orz0$H5Q6LO+.!hY~p2B.N93&EeC7XK8-AF|ZyG%w&UKj' );
define( 'AUTH_SALT',         'k.`=bn>l7Q;s`+1Z^SE9JJuGxc3rw0OK2@I5f+1LF9r3A^pv[z0GCKxZ8Q0orqCr' );
define( 'SECURE_AUTH_SALT',  ':N,<9YZS[)}`u:W)fh@%}S=%0Jlo.cS[8p,Z :x!eXXtoUDbVk+kX!Rn7?$+)yV>' );
define( 'LOGGED_IN_SALT',    'J@L)Nm.dtykn~ONUv?Lho`J49C>#OT(*[J!%}TTU|S7NV LR/AaS7Gwl7VchYgE_' );
define( 'NONCE_SALT',        't/VE{Hx6i+c4)Ze)cvM9pUxB hAWlWx)or6@bb5u@+v!c^ino+:9dGZFBB?<$h:<' );
define( 'WP_CACHE_KEY_SALT', '|1#$}Ub2.D^k>4ycPmrIcy7cdzCYSxOb>B1JV@L!yK4--bT*HXop40BY~hq xU3/' );


/**#@-*/

/**
 * WordPress database table prefix.
 *
 * You can have multiple installations in one database if you give each
 * a unique prefix. Only numbers, letters, and underscores please!
 */
$table_prefix = 'wp_';

/**
 * For developers: WordPress debugging mode.
 *
 * Change this to true to enable the display of notices during development.
 * It is strongly recommended that plugin and theme developers use WP_DEBUG
 * in their development environments.
 *
 * For information on other constants that can be used for debugging,
 * visit the documentation.
 *
 * @link https://wordpress.org/support/article/debugging-in-wordpress/
 */
define( 'WP_DEBUG', false );


/* Add any custom values between this line and the "stop editing" line. */



define( 'FS_METHOD', 'direct' );
define( 'WP_AUTO_UPDATE_CORE', 'minor' );
/* That's all, stop editing! Happy publishing. */

/** Absolute path to the WordPress directory. */
if ( ! defined( 'ABSPATH' ) ) {
	define( 'ABSPATH', __DIR__ . '/' );
}

/** Sets up WordPress vars and included files. */
require_once ABSPATH . 'wp-settings.php';
