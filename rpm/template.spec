Name:           ros-kinetic-hls-lfcd-lds-driver
Version:        0.1.5
Release:        0%{?dist}
Summary:        ROS hls_lfcd_lds_driver package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/hls_lfcd_lds_driver
Source0:        %{name}-%{version}.tar.gz

Requires:       boost-devel
Requires:       ros-kinetic-roscpp
Requires:       ros-kinetic-sensor-msgs
BuildRequires:  boost-devel
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-roscpp
BuildRequires:  ros-kinetic-sensor-msgs

%description
ROS package for LDS(HLS-LFCD2). The LDS (Laser Distance Sensor) is a sensor
sending the data to Host for the simultaneous localization and mapping (SLAM).
Simultaneously the detecting obstacle data can also be sent to Host. HLDS
(Hitachi-LG Data Storage) is developing the technology for the moving platform
sensor such as Robot Vacuum Cleaners, Home Robot, Robotics Lawn Mower Sensor,
etc.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Wed Mar 14 2018 Pyo <pyo@robotis.com> - 0.1.5-0
- Autogenerated by Bloom

* Thu Sep 14 2017 Pyo <pyo@robotis.com> - 0.1.4-0
- Autogenerated by Bloom

* Fri Aug 18 2017 Pyo <pyo@robotis.com> - 0.1.3-0
- Autogenerated by Bloom

* Mon Apr 24 2017 Pyo <pyo@robotis.com> - 0.1.2-0
- Autogenerated by Bloom

* Tue Dec 06 2016 Pyo <pyo@robotis.com> - 0.1.1-1
- Autogenerated by Bloom

* Tue Dec 06 2016 Pyo <pyo@robotis.com> - 0.1.1-0
- Autogenerated by Bloom

