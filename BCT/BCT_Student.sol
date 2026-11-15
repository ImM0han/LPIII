// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract StudentData {
    struct Student {
        uint rollNo;
        string name;
        uint marks;
    }

    Student[] public students;

    function addStudent(uint roll, string memory studentName, uint studentMarks) public {
        students.push(Student(roll, studentName, studentMarks));
    }

    function getStudent(uint index) public view returns (uint, string memory, uint) {
        Student memory s = students[index];
        return (s.rollNo, s.name, s.marks);
    }

    function getCount() public view returns (uint) {
        return students.length;
    }

    receive() external payable {}
    fallback() external payable {}
}