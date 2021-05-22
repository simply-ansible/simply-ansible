#!/bin/bash

# Copyright Kosala Atapattu, 2021 <kosala@kosala.net>

action=$1
repo=$2
work_dir=$3
branch=$4

raise () {
    [ -z $2 ] && {
        category=INFO
        message=$1
    } || {
        category=$1
        message=$2
    }
    timestamp=$(date "+%Y-%m-%d %H:%M:%S")
    [ $? -ne 0 ] && {
        printf ("WARN: 'date' was not found. opting out timestamp")
        timestamp="time unknown"
    }
    printf "[$timestamp] $category: $message"
}

init () {
    repo=$1
    work_dir=$2
    branch=$3

    git --recurse-submodules clone $repo $work_dir

    [ $? -ne 0  ] && {
        raise "ERROR" "error cloning the repo"
        #checking whetherthe work directory is not empty
        [ -z $(ls -a $work_dir) ] || {
            raise "INFO" "Cleaning the work directory..."
            rm -fr $work_dir/* $work_dir/.*
            [ $? -ne 0 ] && {
                raise "ERROR" "Unable to delete the contents of work directory. Calling quits."
                exit 1
            } 
            raise "INFO" "Work directory cleaned"
            git --recurse-submodules clone $repo $work_dir
            [ $? -ne 0 ] && {
                raise "ERROR" "Unable to sync the repo. Calling quits."
                exit 1
            }
        } && {
            raise "ERROR" "Unable to sync the repo. Work dir is empty, but still failing. Calling quits."
            exit 1
        }
    } || {
        cd $work_dir
        git checkout $branch
    }
}

status () {
    work_dir=$1
    cd $work_dir
    git status

    [ $? -eq 0 ] && {
        return 0
    } || {
        return 1
    }
}

sync () {
    work_dir=$1
    branch=$2

    cd $work_dir

    git --recurse-submodules pull origin $branch

    [ $? -ne 0 ] && {
        raise "ERROR" "failed to pull. opting for a re-init."
        return 1
    }

    [ -z ]
    git checkout $branch
}

case $1 in
    setup)
        status($work_dir)
        [ $? -ne 0 ] && {
            print "work directory is not initiated with repo...initiating."
            init($repo, $work_dir, $branch)
        } || {
            print "work directory is good...running a pull"
            sync($work_dir, $branch)
        }
        ;;
    sync)
        sync($work_dir, $branch)



