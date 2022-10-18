#!/bin/bash
folder="$HOME/.bdedbfdbabcbafb56cd51926635d136055035e4dd9c7d1f5003af98/pic"
pic=$(ls $folder/* | shuf -n1)

# values for picture-options: ‘none’, ‘wallpaper’, ‘centered’, ‘scaled’, ‘stretched’, ‘zoom’, ‘spanned’
gsettings set org.gnome.desktop.background picture-options 'scaled'
gsettings set org.gnome.desktop.background picture-uri "file://$pic"
