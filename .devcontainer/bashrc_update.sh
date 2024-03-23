# update .bashrc
# .devcontainer/postCreateCommand.sh
#     apply once at the end of VM creation
#     used in separate file because of quotes in echo command

# aliases
echo "alias ll='ls -alF'" >> ~/.bashrc
echo "alias cd_project='cd $PWD'" >> ~/.bashrc
