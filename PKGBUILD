# Script generated with Bloom
pkgdesc="ROS - ROS package for LDS(HLS-LFCD2). The LDS (Laser Distance Sensor) is a sensor sending the data to Host for the simultaneous localization and mapping (SLAM). Simultaneously the detecting obstacle data can also be sent to Host. HLDS(Hitachi-LG Data Storage) is developing the technology for the moving platform sensor such as Robot Vacuum Cleaners, Home Robot, Robotics Lawn Mower Sensor, etc."
url='http://wiki.ros.org/hls_lfcd_lds_driver'

pkgname='ros-kinetic-hls-lfcd-lds-driver'
pkgver='0.1.5_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('boost'
'ros-kinetic-catkin'
'ros-kinetic-roscpp'
'ros-kinetic-sensor-msgs'
)

depends=('boost'
'ros-kinetic-roscpp'
'ros-kinetic-sensor-msgs'
)

conflicts=()
replaces=()

_dir=hls_lfcd_lds_driver
source=()
md5sums=()

prepare() {
    cp -R $startdir/hls_lfcd_lds_driver $srcdir/hls_lfcd_lds_driver
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/kinetic/setup.bash ] && source /opt/ros/kinetic/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/kinetic \
        -DPYTHON_EXECUTABLE=/usr/bin/python2 \
        -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 \
        -DPYTHON_LIBRARY=/usr/lib/libpython2.7.so \
        -DPYTHON_BASENAME=-python2.7 \
        -DSETUPTOOLS_DEB_LAYOUT=OFF
  make
}

package() {
  cd "${srcdir}/build"
  make DESTDIR="${pkgdir}/" install
}

